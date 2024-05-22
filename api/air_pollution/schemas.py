from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class City(BaseModel):
    """
    Model of city with coordinates.
    """
    id: int = None
    name: str = None
    longitude: float = None
    latitude: float = None

class Category(BaseModel):
    """
    Model of air quality category for each pollutant.
    """
    id: int = None
    quality: str = None
    pollutant: str = None
    min: Optional[int] = None
    max: Optional[int] = None

class AirQualityIndex(BaseModel):
    """
    Model of AQI - air quality index, which is calculated from amount of pollutants.
    """
    id: int = None
    city_id: int = None
    value: float = None
    date: datetime = None

class Parameter(BaseModel):
    """
    Model of pollutant parameter - amount of particular pollutant in μg/m^3.
    """
    id: int = None
    pollutant: str = None
    city_id: int = None
    value: float = None
    category_id: int = None
    date: datetime = None

class Statistics(BaseModel):
    """
    Model of basic statistical parameters of AQI - calculated from 30 days values.
    """
    id: int = None
    city_id: int = None
    month_avg: float = None
    month_var: float = None
    month_min: float = None
    month_max: float = None

class CityComparison(BaseModel):
    """
    Model of order of cities in air quality - for each pollutant.
    """
    id: int = None
    city_id: int = None
    index: int = None
