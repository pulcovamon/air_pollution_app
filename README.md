# Semestral project for school subject TBA
### Web application for vizualization air quality status in several Europe cities
### I am using data from [OpenWeather API](https://openweathermap.org/): 
- **database**: sqlite db containing all data (script for db creation: *database/create_db.py*)
- **data_processing**: service, which scrapes data from [OpenWeater API](https://openweathermap.org/), calculates some basic statistics and saves the data into database
- **api**: service, which exposes endpoints for getting data from database
- **frontend**: react app - *not completed*
- **docs**: web documentation using MkDocs - *not completed*
