from typing import Optional
from sqlalchemy import ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase

"""
Specification of models for using database.
"""

class Base(DeclarativeBase):
    ...


class City(Base):
    """
    Model of city with coordinates.
    """
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    longitude: Mapped[float] = mapped_column(Numeric(7, 4))
    latitude: Mapped[float] = mapped_column(Numeric(7, 4))


class Category(Base):
    """
    Model of air quality category for each pollutant.
    """
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    quality: Mapped[str] = mapped_column(String(10))
    pollutant: Mapped[str] = mapped_column(String(5))
    min: Mapped[Optional[int]] = mapped_column()
    max: Mapped[Optional[int]] = mapped_column()


class AirQualityIndex(Base):
    """
    Model of AQI - air quality index, which is calculated from amount of pollutants.
    """
    __tablename__ = "air_quality_index"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    value: Mapped[float] = mapped_column(Numeric(4, 1))
    date: Mapped[datetime] = mapped_column(DateTime)


class Parameter(Base):
    """
    Model of pollutant parameter - amount of particular pollutant in μg/m^3.
    """
    __tablename__ = "parameter"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pollutant: Mapped[str] = mapped_column(String(5))
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    value: Mapped[float] = mapped_column(Numeric(4, 1))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    date: Mapped[datetime] = mapped_column(DateTime)


class Statistics(Base):
    """
    Model of basic statistical parameters of AQI - calculated from 30 days values.
    """
    __tablename__ = "statistics"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    month_avg: Mapped[float] = mapped_column(Numeric(4, 1))
    month_var: Mapped[float] = mapped_column(Numeric(4, 1))
    month_min: Mapped[float] = mapped_column(Numeric(4, 1))
    month_max: Mapped[float] = mapped_column(Numeric(4, 1))


class CityComparison(Base):
    """
    Model of order of cities in air quality - for each pollutant.
    """
    __tablename__ = "city_comparison"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    index: Mapped[int] = mapped_column()
