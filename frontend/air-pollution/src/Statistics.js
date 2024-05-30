import React, { useEffect, useState } from "react";
import { fetchCityComparison, fetchStatistics } from "./fetch";

export default function Statistics({ selectedCity }) {
    const [comparison, setComparison] = useState([]);
    const [statistics, setStatistics] = useState();
    useEffect(() => {
        const getComparison = async () => {
            try {
                const comparisonData = await fetchCityComparison();
                setComparison(comparisonData);
            } catch (error) {
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
    const statisticsList = (statistics) ? (
        <div>
            <h4>
                Statistical parameters of AQI in {selectedCity.name} (last 30 days)
            </h4>
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
    ) : (
        <h4>No data available</h4>
    )
    const comparisonList = comparison.map((city) => {
        if (city) {
            return(
                <tr>
                    <td>{city.index}</td>
                    <td>{city.city_name}</td>
                    <td>{city.mean}</td>
                </tr>
            )
        }
        return (
            <tr>No data available at this moment</tr>
        )
    })
    return (
        <div className="home">
            {statisticsList}
            <h4>Order of cities</h4>
            <table>
                <tr>
                    <th>Index</th>
                    <th>City</th>
                    <th>AQI</th>
                </tr>
                {comparisonList}
            </table>
        </div>
    )
}