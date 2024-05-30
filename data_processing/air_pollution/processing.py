import pandas as pd
from sqlalchemy import select, and_
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
        categories = self.session.scalars(
            select(Category).where(Category.pollutant==pollutant)
            )
        for category in categories:
            if category.max and value < category.max:
                return category.id
            elif not category.max and value >= category.min:
                return category.id
        raise ValueError(f"Category for pollutant {pollutant} and value {value} was not found!")

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
                Parameter(
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
        start_date = datetime.now() - timedelta(days=30)
        values = self.session.scalars(
            select(AirQualityIndex).where(AirQualityIndex.city_id==city.id).where(AirQualityIndex.date>=start_date)
            ).all()

        df = pd.DataFrame([{"aqi": float(aqi.value)} for aqi in values])
        if not df.empty:
            try:
                record = self.session.query(Statistics).filter(Statistics.city_id == city.id).one()
                record.month_avg = df["aqi"].mean()
                record.month_var = df["aqi"].var()
                record.month_min = df["aqi"].min()
                record.month_max = df["aqi"].max()
                self.session.merge(record)
            except NoResultFound:
                self.session.add(Statistics(
                    city_id = city.id,
                    month_avg = df["aqi"].mean(),
                    month_var = df["aqi"].var(),
                    month_min = df["aqi"].min(),
                    month_max = df["aqi"].max()
                ))
            self.session.commit()

    def calculate_and_save_city_comparison(self) -> None:
        """
        Calculate order of cities ordered by AQI (air quality index).
        """
        statistics = self.session.query(Statistics).all()
        if statistics:
            statistics = {
                "id": [item.city_id for item in statistics],
                "mean": [item.month_avg for item in statistics]
                }
            df = pd.DataFrame(statistics)
            df = df_sorted = df.sort_values(by='mean', ascending=True)
            df["index"] = [i+1 for i in range(len(df["mean"]))]
            for _, row in df.iterrows():
                try:
                    record = self.session.query(CityComparison).filter(CityComparison.city_id == row["id"]).one()
                    record.index = row["index"]
                except NoResultFound:
                    self.session.add(CityComparison(city_id=row["id"], index=row["index"]))
            self.session.commit()
        
