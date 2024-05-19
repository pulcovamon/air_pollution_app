from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.database import Base, engine
from db.models import Category, AirQuality, Statistics, City, CityComparison, Quality, Pollutant


def fill_category_table(session, pollutant):
    ...


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.close()

