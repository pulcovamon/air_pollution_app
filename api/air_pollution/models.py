from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class City(SQLModel, table=True):
    """
    Model of city with coordinates.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    longitude: float
    latitude: float

class Category(SQLModel, table=True):
    """
    Model of air quality category for each pollutant.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    quality: str
    pollutant: str
    min: Optional[int] = None
    max: Optional[int] = None

class AirQualityIndex(SQLModel, table=True):
    """
    Model of AQI - air quality index, which is calculated from amount of pollutants.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    city_id: int = Field(foreign_key="city.id")
    value: float
    date: datetime

class Parameter(SQLModel, table=True):
    """
    Model of pollutant parameter - amount of particular pollutant in μg/m^3.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    pollutant: str
    city_id: int = Field(foreign_key="city.id")
    value: float
    category_id: int = Field(foreign_key="category.id")
    date: datetime

class Statistics(SQLModel, table=True):
    """
    Model of basic statistical parameters of AQI - calculated from 30 days values.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    city_id: int = Field(foreign_key="city.id")
    month_avg: float
    month_var: float
    month_min: float
    month_max: float

class CityComparison(SQLModel, table=True):
    """
    Model of order of cities in air quality - for each pollutant.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    city_id: int = Field(foreign_key="city.id")
    index: int
