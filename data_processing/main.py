from sqlalchemy.orm import sessionmaker

from .air_pollution.models import City
from .air_pollution.scraping import Scraper
from .air_pollution.processing import Data
from .air_pollution.db_connection import engine

"""
Request OpenWeather API for air pollution data,
calculate basic statistics and save data into database.
"""

if __name__ == "__main__":
    db_session = Session = sessionmaker(bind=engine)
    scraper = Scraper(db_session)
    data = Data(db_session)

    for city in db_session.query(City).all():
        # Parameter
        params = scraper.get_parameters(city)
        data.save_aqi_into_db(params)

        # AirQualityIndex
        aqi = scraper.get_aqi(city)
        data.save_aqi_into_db(aqi)

        # Statistics
        data.calculate_and_save_statistics(city)

    # CityComparison
    data.calculate_and_save_city_comparison()

    db_session.close()