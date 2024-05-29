from sqlalchemy.orm import sessionmaker

from air_pollution.models import City
from air_pollution.scraping import Scraper
from air_pollution.processing import Data
from air_pollution.db_connection import engine

"""
Request OpenWeather API for air pollution data,
calculate basic statistics and save data into database.
"""

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    db_session = Session()
    print("database connected")
    scraper = Scraper(db_session)
    data = Data(db_session)

    for city in db_session.query(City).all():
        print(f"processing city {city.name}")
        # datetime
        datetime = scraper.get_datetime(city)

        # Parameter
        params = scraper.get_parameters(city)
        data.save_parameters_into_db(city, params, datetime)

        # AirQualityIndex
        aqi = scraper.get_aqi(city)
        data.save_aqi_into_db(city, aqi, datetime)

        # Statistics
        data.calculate_and_save_statistics(city)
        print("city processed")

    # CityComparison
    print("processing city comparison")
    data.calculate_and_save_city_comparison()
    print("city comparison processed")

    db_session.close()