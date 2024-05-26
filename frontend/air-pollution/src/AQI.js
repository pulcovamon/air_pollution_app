import React, { useEffect, useState } from 'react';

import Chart from "./Chart";
import { fetchAirQualityIndex } from './fetch';

export default function Parameters({ selectedCity }) {
    const [airQualityIndex, setAirQualityIndex] = useState([]);
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
          getAirQualityIndex();
        }
      }, [selectedCity]);
    return (
        <div>
            <Chart data={airQualityIndex} title={ `Air Quality Index in ${selectedCity}` } />;
        </div>
    );
}