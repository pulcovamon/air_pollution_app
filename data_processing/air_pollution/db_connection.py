from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://user:pass@db:3306/AirQuality"

engine = create_engine(DATABASE_URL)