import React, { useEffect, useState } from 'react';

import Chart from "./Chart";
import { fetchAirQualityParameters } from './fetch';

export default function Parameters({ selectedCity }) {
    const [airQualityParameters, setAirQualityParameters] = useState(null);

    useEffect(() => {
        const getAirQualityParameters = async () => {
            if (selectedCity) {
                try {
                    const paramsData = await fetchAirQualityParameters(selectedCity.id);
                    console.log('Fetched Air Quality Parameters:', paramsData);
                    setAirQualityParameters(paramsData);
                } catch (error) {
                    console.error('Error fetching air quality parameters:', error);
                }
            }
        };
        getAirQualityParameters();
    }, [selectedCity]);

    const pollutants = ["co", "no2", "so2", "o3", "pm10", "pm2_5"];

    const pollutantCharts = pollutants.map((pollutant) => {
        if (!airQualityParameters || !airQualityParameters[pollutant]) {
            return (
                <li key={pollutant}>
                    <p>No data available for {pollutant}</p>
                </li>
            );
        }
        return (
            <li key={pollutant}>
                <Chart
                    data={airQualityParameters[pollutant]}
                    title={`Amount of ${pollutant} in ug/m^3 in ${selectedCity.name}`}
                />
            </li>
        );
    });

    return (
        <div>
            <ul>
                {pollutantCharts}
            </ul>
        </div>
    );
}
