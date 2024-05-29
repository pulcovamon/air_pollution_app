import React, { useEffect, useState } from "react";
import { fetchCityComparison, fetchStatistics } from "./fetch";

export default function Statistics({ selectedCity }) {
    const [comparison, setComparison] = useState([]);
    const [statistics, setStatistics] = useState([]);
    useEffect(() => {
        const getComparison = async () => {
            try {
                const comparisonData = await fetchCityComparison();
                setComparison(comparisonData);
            } catch {
                console.error("Error fetching city comparison:", error);
            }
        }
        getComparison();
    })
    useEffect(() => {
        if (selectedCity) {
          const getStatistics = async () => {
            try {
              const statisticsData = await fetchStatistics(selectedCity.id);
              setStatistics(statisticsData);
            } catch (error) {
              console.error('Error fetching statistics:', error);
            }
          };
          getStatistics();
        }
      }, [selectedCity]);
    const statisticsList = (
        <div>
            <h2>
                Statistical parameters of AQI in {selectedCity.name} (last 30 days)
            </h2>
            <ul>
                <li>
                    Average AQI: <b>{statistics.month_avg}</b>
                </li>
                <li>
                    Variance of AQI: <b>{statistics.month_var}</b>
                </li>
                <li>
                    Maximum AQI: <b>{statistics.month_max}</b>
                </li>
                <li>
                    Minimum AQI: <b>{statistics.month_min}</b>
                </li>
            </ul>
        </div>
    )
    const comparisonList = comparison.map((city) => {
        const cityName = city.name;
        const index = city.index;
        const aqi = city.aqi;
    })
    return (
        <div className="home">
            <h2>Order of cities</h2>
            <ul>
                <li></li>
            </ul>
            <br />
            {statisticsList}
        </div>
    )
}