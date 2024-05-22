export async function fetchCities() {
    const response = await fetch('0.0.0.0:8000/air_pollution_api/cities');
    if (!response.ok) {
      throw new Error('Cities are not available');
    }
    return response.json();
  }
  
  export async function fetchAirQualityIndex(cityId) {
    const response = await fetch(`0.0.0.0:8000/air_pollution_api/air_quality_index/${cityId}`);
    if (!response.ok) {
      throw new Error(`AQI in city with ID ${cityId} is not avaliable.`);
    }
    return response.json();
  }
  
  export async function fetchAirQualityParameters(cityId) {
    const response = await fetch(`0.0.0.0:8000/air_pollution_api/air_quality_parameters/${cityId}`);
    if (!response.ok) {
      throw new Error(`Air quality parameters in city with ID ${cityId} is not avaliable.`);
    }
    return response.json();
  }

  export async function fetchStatistics(cityId) {
    const response = await fetch(`0.0.0.0:8000/air_pollution_api/statistics/${cityId}`);
    if (!response.ok) {
        throw new Error(`Statistics in city with ID ${cityId} is not avaliable.`);
    }
    return response.json();
  }

  export async function fetchCityComparison() {
    const response = await fetch(`0.0.0.0:8000/air_pollution_api/city_comparison/${cityId}`);
    if (!response.ok) {
        throw new Error(`City comparison is not avaliable.`);
    }
    return response.json();
  }
  