import React, { useEffect, useState } from 'react';
import Chart from "./Chart";
import { fetchAirQualityParameters } from './fetch';

function convertPollutantName(abbreviation) {
    switch (abbreviation) {
        case "co":
            return "CO";
        case "no2":
            return "NO₂";
        case "so2":
            return "SO₂";
        case "o3":
            return "O₃";
        case "pm10":
            return "PM₁₀";
        case "pm2_5":
            return "PM₂.₅";
        default:
            return abbreviation.toUpperCase();
    }
};

export default function Parameters({ selectedCity }) {
    const [airQualityParameters, setAirQualityParameters] = useState({});
    const pollutants = ["co", "no2", "so2", "o3", "pm10", "pm2_5"];

    useEffect(() => {
        const getAirQualityParameters = async (parameter) => {
            if (selectedCity) {
                try {
                    const paramsData = await fetchAirQualityParameters(selectedCity.id, parameter);
                    setAirQualityParameters(prevState => ({
                        ...prevState,
                        [parameter]: paramsData
                    }));
                } catch (error) {
                    console.error(`Error fetching ${parameter} data:`, error);
                }
            }
        };

        pollutants.forEach(pollutant => getAirQualityParameters(pollutant));
    }, [selectedCity]);

    const pollutantCharts = pollutants.map((pollutant) => {
        const data = airQualityParameters[pollutant];
        if (!data) {
            return (
                <li key={pollutant}>
                    <p>No data available for {convertPollutantName(pollutant)}</p>
                </li>
            );
        }
        return (
            <li key={pollutant}>
                <Chart
                    data={data}
                    title={`Amount of ${convertPollutantName(pollutant)} in μg/m³`}
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
