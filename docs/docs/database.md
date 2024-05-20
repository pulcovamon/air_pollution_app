# Database

The project uses a SQLite database to store data.

## Models

### City

Represents a city with coordinates.

- `id`: Integer, primary key.
- `name`: String, name of the city.
- `longitude`: Float, longitude of the city.
- `latitude`: Float, latitude of the city.

### AirQualityIndex

Represents the AQI (air quality index) for a city.

- `id`: Integer, primary key.
- `city_id`: Integer, foreign key to `City`.
- `value`: Float, air quality index value.
- `date`: DateTime, date of the record.

### Category

Represents an air quality category for each pollutant.

- `id`: Integer, primary key.
- `quality`: String, quality description.
- `pollutant`: String, name of the pollutant.
- `min`: Optional Integer, minimum value of the category.
- `max`: Optional Integer, maximum value of the category.

### Parameter

Represents parameters (amount of each pollutant) for a city.

- `id`: Integer, primary key.
- `pollutant`: String, name of the pollutant.
- `city_id`: Integer, foreign key to `City`.
- `value`: Float, value of the pollutant parameter.
- `category_id`: Integer, foreign key to `Category`.
- `date`: DateTime, date of the record.

### Statistics

Represents basic statistical parameters of AQI for a city (calculated from last 30 days).

- `id`: Integer, primary key.
- `city_id`: Integer, foreign key to `City`.
- `month_avg`: Float, monthly average AQI.
- `month_var`: Float, monthly variance of AQI.
- `month_min`: Float, minimum AQI of the month.
- `month_max`: Float, maximum AQI of the month.

### CityComparison

Represents the order of cities ordered by AQI.

- `id`: Integer, primary key.
- `city_id`: Integer, foreign key to `City`.
- `index`: Integer, the ranking index of the city based on air quality.
