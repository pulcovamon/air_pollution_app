import requests
import os
from datetime import datetime
from sqlalchemy import select

from .models import City, Category, AirQualityIndex, Parameter, Statistics, CityComparison

"""
Web scraping - getting data from OpenWeather API"
"""

class Scraper:
    uri = "http://api.openweathermap.org/data/2.5/air_pollution"
    api_key = os.getenv("API_KEY", "001c2554cc486bf50b3c05b32d468e1b")
    uri = "http://api.openweathermap.org"

    def __init__(self, db_session):
        self.session = db_session
        self.data = {}

    def _request_api(self, city: City) -> dict:
        """
        Send get request to OpenWeather API and get data for the city.

        Args:
            city (City): city object with coordinates

        Returns:
            dict: response
        """
        city = self.session.execute(select(City).where(City.name == city.name)).scalars().first()

        if not city:
            raise ValueError("City not found in database!")

        uri = f"{self.uri}/data/2.5/air_pollution?lat={city.latitude}&lon={city.longitude}&appid={self.api_key}"

        response = requests.get(uri)
        if not response.ok:
            response.raise_for_status()
        return response.json()["list"][0]


    def get_parameters(self, city: City) -> dict:
        """
        Get current value of a pollutant in the given city.

        Args:
            city (City): city object with coordinates

        Returns:
            dict: parameter value
        """
        if city.name not in self.data:
            self.data[city.name] = self._request_api(city)
        parameters = {key: value for key, value in self.data[city.name]["components"].items() if key in ["so2", "no2", "pm2_5", "pm10", "o3", "co"]}
        print(parameters)
        return parameters

    def get_aqi(self, city: City) -> float:
        """
        Get current value of AQI (air quality index) in the given city.

        Args:
            city (City): city object with coordinates

        Returns:
            float: AQI value
        """
        if city.name not in self.data:
            self.data[city.name] = self._request_api(city)
        return self.data[city.name]["main"]["aqi"]

    def get_datetime(self, city: City) -> int:
        """
        Get unix timestamp of last reques.

        Args:
            city (City): city object with coordinates
            parameter (str): name of pollutant

        Returns:
            int: unix timestamp
        """
        if city.name not in self.data:
            self.data[city.name] = self._request_api(city)
        return datetime.fromtimestamp(self.data[city.name]["dt"])

    def clear_data(self):
        """
        Reinitialize data variable.
        """
        self.data = {}
