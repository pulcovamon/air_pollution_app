from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

"""
Script for database specification.
"""

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:pass@0.0.0.0:3306/AirQuality"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()