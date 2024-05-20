import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function App() {
  const [cities, setCities] = useState([]);
  const [airQualityIndex, setAirQualityIndex] = useState([]);
  const [airQualityParameters, setAirQualityParameters] = useState([]);
  const [statistics, setStatistics] = useState({});
  const [cityComparison, setCityComparison] = useState([]);

  useEffect(() => {
    fetchCities();
    fetchAirQualityIndex();
    fetchAirQualityParameters();
    fetchStatistics();
    fetchCityComparison();
  }, []);

  async function fetchCities() {
    try {
      const response = await axios.get('http://localhost:8000/air_pollution_api/cities');
      setCities(response.data);
    } catch (error) {
      console.error('Error fetching cities:', error);
    }
  };

  async function fetchAirQualityIndex(cityId) {
    try {
      const response = await axios.get(`http://localhost:8000/air_pollution_api/air_quality_index/${cityId}`);
      setAirQualityIndex(response.data);
    } catch (error) {
      console.error('Error fetching air quality index:', error);
    }
  };

  async function fetchAirQualityParameters(cityId) {
    try {
      const response = await axios.get(`http://localhost:8000/air_pollution_api/air_quality_parameters/${cityId}`);
      setAirQualityParameters(response.data);
    } catch (error) {
      console.error('Error fetching air quality parameters:', error);
    }
  };

  async function fetchStatistics(cityId) {
    try {
      const response = await axios.get(`http://localhost:8000/air_pollution_api/statistics/${cityId}`);
      setStatistics(response.data);
    } catch (error) {
      console.error('Error fetching statistics:', error);
    }
  };

  async function fetchCityComparison() {
    try {
      const response = await axios.get('http://localhost:8000/air_pollution_api/city_comparison');
      setCityComparison(response.data);
    } catch (error) {
      console.error('Error fetching city comparison:', error);
    }
  };

  return (
    <div>
      <h1>Cities</h1>
      <ul>
        {cities.map((city, index) => (
          <li key={index}>{city.name}</li>
        ))}
      </ul>

      <h1>Air Quality Index</h1>
      <ul>
        {airQualityIndex.map((indexData, index) => (
          <li key={index}>{indexData.value}</li>
        ))}
      </ul>

      <h1>Air Quality Parameters</h1>
      <ul>
        {airQualityParameters.map((parameter, index) => (
          <li key={index}>{parameter.value}</li>
        ))}
      </ul>

      <h1>Statistics</h1>
      <p>{statistics.city_id}</p>

      <h1>City Comparison</h1>
      <ul>
        {cityComparison.map((comparison, index) => (
          <li key={index}>{comparison.city_id}</li>
        ))}
      </ul>
    </div>
  );
};
