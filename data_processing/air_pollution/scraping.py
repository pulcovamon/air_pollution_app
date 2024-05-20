import requests
import os

from .models import City, Category, AirQualityIndex, Parameter, Statistics, CityComparison

"""
Web scraping - getting data from OpenWeather API"
"""

class Scraper:
    uri = "http://api.openweathermap.org/data/2.5/air_pollution"
    api_key = os.getenv("API_KEY")
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
        longitude = self.session.scalars(select(City.longitude).where(City.name==city)).one()
        latitude = self.session.scalars(select(City.latitude).where(City.name==city)).one()
        uri = f"{self.uri}/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={self.api_key}"

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
        return data[city]["parameters"]

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
        return data["city"]["main"]["aqi"]

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
        return data[city]["dt"]

    def clear_data(self):
        """
        Reinitialize data variable.
        """
        self.data = {}
