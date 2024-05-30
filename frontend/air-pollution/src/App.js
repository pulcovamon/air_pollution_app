import React, { useEffect, useState } from 'react';
import { fetchCities } from './fetch';
import Navbar from './Navbar';
import AQI from './AQI';
import Parameters from './Parameters';
import CitySelect from './Cities';
import Home from './Home';
import Statistics from './Statistics';

export default function App() {
  const [cities, setCities] = useState([]);
  const [selectedCity, setSelectedCity] = useState(null);
  const [selectedScreen, setSelectedScreen] = useState("Home");

  useEffect(() => {
    async function getCities() {
      try {
        const citiesData = await fetchCities();
        setCities(citiesData);
      } catch (error) {
        console.error('Error fetching cities:', error);
      }
    }
    getCities();
  }, []);

  useEffect(() => {
    if (cities.length > 0 && !selectedCity) {
      setSelectedCity(cities[0]);
    }
  }, [cities]);

  function handleCitySelection(e) {
    const selectedCityId = parseInt(e.target.value);
    const selectedCity = cities.find(city => city.id === selectedCityId);
    setSelectedCity(selectedCity);
    console.log("Selected City:", selectedCity); // Debugging line
  }  

  function handleScreenSelection(screenComponent) {
    setSelectedScreen(screenComponent);
  }

  return (
    <div className='App'>
      <Navbar handleSelection={handleScreenSelection} />
      {selectedScreen !== 'Home' && <CitySelect handleSelection={handleCitySelection} cities={cities} />}
      <div className="chart-container">
        {selectedScreen === 'Home' && <Home />}
        {selectedScreen === 'AQI' && <AQI selectedCity={selectedCity} />}
        {selectedScreen === 'Parameters' && <Parameters selectedCity={selectedCity} />}
        {selectedScreen === 'Statistics' && <Statistics selectedCity={selectedCity} />}
      </div>
    </div>
  );
}
