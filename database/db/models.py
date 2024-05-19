import enum
from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

from .database import Base


class Quality(enum.Enum):
    GOOD = "Good"
    FAIR = "Fair"
    MODERATE = "Moderate"
    POOR = "Poor"
    VERY_POOR = "Very poor"


class Pollutant(enum.Enum):
    SO2 = "SO2"
    NO2 = "NO2"
    PM10 = "PM10"
    PM2_5 = "PM2.5"
    O3 = "O3"
    CO = "CO"


class City(Base):
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    longitude: Mapped[float] = mapped_column(Decimal(6, 4))
    latitude: Mapped[float] = mapped_column(Decimal(6, 4))


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    quality: Mapped[Quality] = mapped_column(Enum(Quality))
    index: Mapped[int] = mapped_column()
    pollutant: Mapped[Pollutant] = mapped_column(Enum(Pollutant))
    min: Mapped[Optional[int]] = mapped_column()
    max: Mapped[Optional[int]] = mapped_column()


class AirQualityIndex(Base):
    __tablename__ = "air_quality_index"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    value: Mapped[falot] = mapped_column(Decimal(4, 1))
    date: Mapped[datetime] = mapped_column(DateTime)


class Parameter(Base):
    __tablename__ = "parameter"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pollutant: Mapped[Pollutant] = mapped_column(Enum(Pollutant))
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    value: Mapped[int] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    date: Mapped[datetime] = mapped_column(DateTime)


class Statistics(Base):
    __tablename__ = "statistics"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pollutant: Mapped[Pollutant] = mapped_column(Enum(Pollutant))
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    month_avg: Mapped[int] = mapped_column()
    month_var: Mapped[int] = mapped_column()
    month_min: Mapped[int] = mapped_column()
    month_max: Mapped[int] = mapped_column()


class CityComparison(Base):
    __tablename__ = "city_comparison"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pollutant: Mapped[Pollutant] = mapped_column(Enum(Pollutant))
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    index: Mapped[int] = mapped_column()
