import pandas as pd
from sqlalchemy import select
from datetime import datetime, timedelta
from sqlalchemy.orm.exc import NoResultFound

from .models import City, Category, AirQualityIndex, Parameter, Statistics, CityComparison

"""
Data processing and saving into database.
"""

class Data:
    
    def __init__(self, db_session):
        self.session = db_session

    def save_aqi_into_db(self, city: City, value: float, date: int):
        """
        Save AQI (air quality index) into database.

        Args:
            city (City): city object
            value (float): AQI value
            date (int): unix timestamp
        """
        self.session.add(AirQualityIndex(
            city_id = city.id,
            value = value,
            date = date
            )
        )
        self.session.commit()

    def _get_category(self, pollutant: str, value: float) -> str:
        """
        Get category of air quality for particular pollutant.

        Args:
            pollutant (str): name of pollutant
            value (float): amount of pollutant

        Returns:
            str: category id
        """
        category = self.session.scalars(
            select(Category).where(Category.pollutant==pollutant)
            )
        for category in categories:
            category = self.session.get(Category, id=category)
            if category.max and value < category.max:
                return category.id
        return category.id

    def save_parameters_into_db(self, city: City, parameters: dict, date: int) -> None:
        """
        Save parameter (pollutant, value and category) into database.

        Args:
            city (City): city object
            parameters (Dict[str, float]): dictionary of names of parameters and values
            date (int): unix timestamp
        """
        df = pd.DataFrame(parameters.items(), columns=['pollutant', 'value'])
        # add new columns category, city_id and date
        df['category_id'] = df.apply(lambda row: self._get_category(row['pollutant'], row['value']), axis=1)
        df['city_id'] = city.id
        df['date'] = date

        for _, row in df.iterrows():
            self.session.add(
                parameter = Parameter(
                pollutant=row['pollutant'],
                city_id=row['city_id'],
                value=row['value'],
                category_id=row['category_id'],
                date=row['date']
                )
            )
        self.session.commit()

    def calculate_and_save_statistics(self, city: City) -> None:
        """
        Calculate mean, max, min and var value of AQI in last month.

        Args:
            city (City): city object
        """
        end_date = datetime.utcfromtimestamp(datetime.now())
        start_date = datetime.utcfromtimestamp(datetime.now() - timedelta(days=30))
        query = self.session.query(AirQualityIndex).join(City).filter(
            and_(
                AirQualityIndex.city_id == City.id,
                AirQualityIndex.date >= start_date,
                AirQualityIndex.date <= end_date
            )
        )
        df = pd.DataFrame([{"aqi": aqi.value} for aqi in query.all()])
        if not df.empty:
            try:
                record = session.query(Statistics).filter(Statistics.city_id == city.id).one()
                record.month_avg = df["value"].mean()
                record.month_var = df["value"].var()
                record.month_min = df["value"].min()
                record.month_max = df["value"].max()
                self.session.merge(existing_record)
            except NoResultFound:
                self.session.add(Statistics(
                    city_id = city.id,
                    month_avg = df["value"].mean(),
                    month_var = df["value"].var(),
                    month_min = df["value"].min(),
                    month_max = df["value"].max()
                ))
            session.commit()

    def calculate_and_save_city_comparison(self) -> None:
        """
        Calculate order of cities ordered by AQI (air quality index).
        """
        city_df = pd.read_sql(self.session.query(City).statement, session.bind)
        aqi_df = pd.read_sql(self.session.query(AirQualityIndex).statement, session.bind)
        aqi_df['date'] = pd.to_datetime(aqi_df['date'])
        latest_aqi_df = aqi_df.sort_values(by='date', ascending=False).groupby('city_id').first().reset_index()
        merged_df = pd.merge(latest_aqi_df, city_df, left_on='city_id', right_on='id', suffixes=('_aqi', '_city'))
        mean_aqi_df = merged_df.groupby('name')['value'].mean().reset_index()
        sorted_cities = mean_aqi_df.sort_values(by='value').reset_index(drop=True)
        sorted_cities['index'] = sorted_cities.index + 1
        for index, row in sorted_cities.iterrows():
            self.session.add(CityComparison(
                city_id = row['name'],
                index = row['index']
                )
            )
        self.session.commit()
