import React, { useEffect, useState } from 'react';
import { fetchCities } from './fetch';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Navbar from './Navbar';
import AQI from './AQI';
import Parameters from './Parameters'
import CitySelect from './Cities';

export default function App() {
  const [cities, setCities] = useState([]);
  const [selectedCity, setSelectedCity] = useState(null);

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

  function handleSelection(e) {
    setSelectedCity(cities.find(city => city.id === parseInt(e.target.value)));
  }

  return (
    <div className="App">
      <Router>
        <Navbar />
        <main className="main-content">
          <Routes>
            <Route path="/aqi" element={<AQI selectedCity={selectedCity} />} />
            <Route path="/parameters" element={<Parameters selectedCity={selectedCity} />} />
            {/* Define other routes that you need*/}
          </Routes>
        </main>
      </Router>
      <CitySelect handleSelection={handleSelection} cities={cities} />
    </div>
  );  
}
