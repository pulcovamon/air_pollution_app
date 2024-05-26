import React, { useEffect, useState } from 'react';

import Chart from "./Chart";
import { fetchAirQualityParameters } from './fetch';

export default function Parameters({ selectedCity }) {
    const [airQualityParameters, setAirQualityParameters] = useState([]);
    useEffect(() => {
        if (selectedCity) {
          const getAirQualityParameters = async () => {
            try {
              const paramsData = await fetchAirQualityParameters(selectedCity.id);
              setAirQualityParameters(paramsData);
            } catch (error) {
              console.error('Error fetching air quality parameters:', error);
            }
          };
          getAirQualityParameters();
        }
      }, [selectedCity]);
    const pollutants = ["co", "no2", "so2", "o3", "pm10", "pm2_5"];
    pollutants.forEach( (pollutant) => {
        pollutant = <Chart data={airQualityParameters[pollutant]} title={ `Amount of ${pollutant} in ug/m^3 in ${selectedCity.name}` } />;
    });

    return (
        <div>
            {pollutants}
        </div>
    )
}