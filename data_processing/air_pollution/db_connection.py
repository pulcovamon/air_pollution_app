from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://user:pass@db:3306/AirQuality"

engine = create_engine(DATABASE_URL)