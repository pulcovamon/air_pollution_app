import React, { useEffect, useState } from 'react';

import Chart from "./Chart";
import { fetchAirQualityIndex } from './fetch';

function Today({ airQualityIndex }) {
  if (airQualityIndex && airQualityIndex.length > 0) {
    return <h4>{`Today: ${airQualityIndex[airQualityIndex.length-1].value}`}</h4>
  }
  return <h4>Today: No data</h4>
}

export default function AQI({ selectedCity }) {
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
            <p>
              The Air Quality Index (<b>AQI</b>) is used for reporting daily air quality.
              It tells you how clean or polluted your air is, and what associated health effects might be a concern for you.
              The AQI focuses on health effects you may experience within a few hours or days after breathing polluted air.
              EPA calculates the AQI for five major air pollutants regulated by the Clean Air Act:
              ground-level ozone, particle pollution (also known as particulate matter), carbon monoxide, sulfur dioxide, and nitrogen dioxide.
              For each of these pollutants, EPA has established national air quality standards to protect public health.
              Ground-level ozone and airborne particles are the two pollutants that pose the greatest threat to human health in this country.
              <br />
              <b>Source: <a href="https://www.weather.gov/safety/airquality-aqindex">National Weather Service</a></b>
            </p>
            <Today airQualityIndex={airQualityIndex} />
            <br />
            <Chart data={airQualityIndex} title={ "Air Quality Index" } />
        </div>
    );
}