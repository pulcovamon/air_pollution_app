from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import os
import requests
from datetime import datetime, timedelta
import calendar
import json
import traceback
from typing import Tuple

from db.database import Base, engine
from db.models import Category, AirQualityIndex, Parameter, Statistics, City, CityComparison


"""
Script for database creation.
"""


class DatabaseFiller:
    """
    Start database session and enable filling tables, rollback and commit.
    """
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.uri = "http://api.openweathermap.org"
        self.api_key = os.getenv("API_KEY")
        self.cities = ["Prague", "London", "Paris", "Berlin", "Rome"]

    def fill_all_tables(self) -> None:
        """
        Fill all tables, which shoud be filled before start of application.
        """
        self.fill_city_table()
        self.fill_category_table()
        self.fill_aqi_and_parameter_tables()

    def request_longitute_latitude(self, city_name: str) -> Tuple[float, float]:
        """
        Send get request to OpenWeather API and get longiture and latitude of the city.

        Args:
            city_name (str): name of the city in english.

        Returns:
            Tuple(flaot, float): longitude and latitude
        """
        uri = f"{self.uri}/geo/1.0/direct?q={city_name}&limit=5&appid={self.api_key}"
        response = requests.get(uri)
        if not response.ok:
            response.raise_for_status()
        response = response.json()[0]
        return response["lon"], response["lat"]

    def request_history_data(self, city: str, date: datetime) -> dict:
        """
        Send get request to OpenWeather API and get data for the city in particular date.

        Args:
            city (str): name of the city in english.
            date (datetime): date of requested historical data.

        Returns:
            dict: response
        """
        start = calendar.timegm(date.utctimetuple())
        date = date + timedelta(days=1)
        end = calendar.timegm(date.utctimetuple())
        longitude = self.session.scalars(select(City.longitude).where(City.name==city)).one()
        latitude = self.session.scalars(select(City.latitude).where(City.name==city)).one()
        uri = f"{self.uri}/data/2.5/air_pollution/history?lat={latitude}&lon={longitude}&start={start}&end={end}&appid={self.api_key}"
        response = requests.get(uri)
        if not response.ok:
            response.raise_for_status()
        return response.json()["list"][0]

    def fill_category_table(self) -> None:
        """
        Fill in table with categories from json file.
        """
        with open("air_quality_index_levels.json") as f:
            categories = json.load(f)

        for pollutant, qualities in categories.items():
            for quality, values in qualities.items():
                self.session.add(Category(quality=quality, pollutant=pollutant, min=values["min"], max=values["max"]))

    def get_category(self, pollutant: str, value: float) -> str:
        """
        Get category of air quality for particular pollutant.

        Args:
            pollutant (str): name of pollutant
            value (float): amount of pollutant

        Returns:
            str: category name
        """
        with open("air_quality_index_levels.json") as f:
            categories = json.load(f)[pollutant]
            for category, values in categories.items():
                if values["max"] and value <= values["max"]:
                    return category
            return "Very poor"

    def fill_aqi_and_parameter_tables(self) -> None:
        """
        Fill in AQI and parameter tables with historical data (30 days)
        """
        for city in self.cities:
            date = datetime.now() - timedelta(days=31)
            for _ in range(30):
                data = self.request_history_data(city, date)
                city_id = self.session.scalars(select(City.id).where(City.name == city)).one()
                utc_date = datetime.utcfromtimestamp(data["dt"])
                self.session.add(AirQualityIndex(city_id=city_id, date=utc_date, value=data["main"]["aqi"]))
                for pollutant, value in data["components"].items():
                    if pollutant not in ["nh3", "no"]:
                        category_id = self.session.scalars(select(Category.id).where(Category.pollutant==pollutant).where(Category.quality == self.get_category(pollutant, value))).one()
                        self.session.add(Parameter(pollutant=pollutant, city_id=city_id, value=value, category_id=category_id, date=utc_date))
                date += timedelta(days=1)

    def fill_city_table(self):
        """
        Fill in city table with city names and coordinates.
        """
        for city in self.cities:
            lon, lat = self.request_longitute_latitude(city)
            print(f"pridavam {city}")
            self.session.add(City(name=city, longitude=lon, latitude=lat))

    def rollback(self):
        """
        Rollback database changes.
        """
        self.session.rollback()

    def commit_and_close(self):
        """
        Commit database changes and close the session.
        """
        self.session.commit()
        self.session.close()


if __name__ == "__main__":
    # reinitialize database
    print("mazu")
    Base.metadata.drop_all(engine)
    print("vytvarim")
    Base.metadata.create_all(engine)
    
    filler = DatabaseFiller()
    try:
        filler.fill_all_tables()
        filler.commit_and_close()
        print("vytvoreno")
    except Exception:
        filler.rollback()
        traceback.print_exc()
