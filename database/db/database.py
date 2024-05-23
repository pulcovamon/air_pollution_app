from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

"""
Script for database specification.
"""

DATABASE_URL = "mysql+mysqlconnector://user:pass@db:3306/AirQuality"

engine = create_engine(DATABASE_URL)

Base = declarative_base()