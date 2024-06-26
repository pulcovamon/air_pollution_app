# API Documentation

## Endpoints

### GET /cities

Returns list of available cities.

**Response:**
- List of all available cities.

### GET /air_quality_index/{city_id}

Returns AQI (air quality index) for a specified city.

**Parameters:**
- `city_id` (int): The id of the city.

**Response:**
- List of AQI (air quality index) records for the city.

### GET /air_quality_parameters/{city_id}/{parameter}

Returns the air quality parameters (amount of each pollutant) for a specified city.

**Parameters:**
- `city_id` (int): The ID of the city.
- `parameter` (str): name of parameter => [co, no3, so3, o3, pm10, pm2_5]

**Response:**
- List of records of quantities of the paramter for the city.

### GET /statistics/{city_id}

Returns basic statistic parameters calculated from last month.

**Parameters:**
- `city_id` (int): The ID of the city.

**Response:**
- Basic statistic parameters of AQI (min, max, mean, var).

### GET /city_comparison

Returns order of cities order by AQI.

**Response:**
- List of cities with indices of order.
