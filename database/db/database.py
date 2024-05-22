from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

"""
Script for database specification.
"""

SQLALCHEMY_DATABASE_URL = "mysql:///?User=root&Password=pass&Database=AirQuality&Server=myServer&Port=3306"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()