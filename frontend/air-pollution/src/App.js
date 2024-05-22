import React, { useEffect, useState } from 'react';
import { fetchCities, fetchAirQualityIndex, fetchAirQualityParameters, fetchStatistics, fetchCityComparison } from './fetch';
import ChartComponent from './ChartComponents';

export default function App() {
  const [cities, setCities] = useState([]);
  const [selectedCity, setSelectedCity] = useState(null);
  const [airQualityIndex, setAirQualityIndex] = useState([]);
  const [airQualityParameters, setAirQualityParameters] = useState([]);

  useEffect(() => {
    async function getCities() {
      try {
        const citiesData = await fetchCities();
        setCities(citiesData);
      } catch (error) {
        console.error('Error fetching cities:', error);
      }
    };
    getCities();
  }, []);

  useEffect(() => {
    if (selectedCity) {
      const getAirQualityIndex = async () => {
        try {
          const aqiData = await fetchAirQualityIndex(selectedCity.id);
          setAirQualityIndex(aqiData);
        } catch (error) {
          console.error('Error fetching air quality index:', error);
        }
      };
      const getAirQualityParameters = async () => {
        try {
          const paramsData = await fetchAirQualityParameters(selectedCity.id);
          setAirQualityParameters(paramsData);
        } catch (error) {
          console.error('Error fetching air quality parameters:', error);
        }
      };
      getAirQualityIndex();
      getAirQualityParameters();
    }
  }, [selectedCity]);

  return (
    <div className="App">
      <h1>Air Quality Monitoring</h1>
      <select onChange={(e) => setSelectedCity(cities.find(city => city.id === parseInt(e.target.value)))}>
        <option value="">Select a city</option>
        {cities.map((city) => (
          <option key={city.id} value={city.id}>{city.name}</option>
        ))}
      </select>
      {selectedCity && (
        <div>
          <h2>Air Quality Index for {selectedCity.name}</h2>
          <ChartComponent data={airQualityIndex} title="Air Quality Index" />
          <h2>Air Quality Parameters for {selectedCity.name}</h2>
          <ChartComponent data={airQualityParameters} title="Air Quality Parameters" />
        </div>
      )}
    </div>
  );
}
