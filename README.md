# Semestral project for school subject TBA
### Web application for vizualization air quality status in several European and Asian cities
### I am using data from [OpenWeather API](https://openweathermap.org/): 
- **database**: mysql db containing all data (script for db creation (its own container): *database/create_db.py*)
- **data_processing**: service, which scrapes data from [OpenWeater API](https://openweathermap.org/), calculates some basic statistics and saves the data into database
- **api**: service, which exposes endpoints for getting data from database
- **frontend**: react app, which shows air pollution data in charts
- **docs**: web documentation using MkDocs - describes each part of the app
