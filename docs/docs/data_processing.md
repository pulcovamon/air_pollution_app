# Data Processing

The data processing module is responsible for scraping air quality data, calculating statistics, and saving data into the database.

## Workflow

1. Scrape data from [OpenWeather API](https://openweathermap.org).
2. Save air quality index and parameters into the database.
3. Calculate and save statistics.
4. Calculate and save city comparisons.

## Code Overview

- **scraping.py**: Contains the `Scraper` class for requesting data.
- **processing.py**: Contains the `Data` class for data processing and saving into database.
