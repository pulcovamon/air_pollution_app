from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://root:root@db:3306/AirQuality"

engine = create_engine(DATABASE_URL)