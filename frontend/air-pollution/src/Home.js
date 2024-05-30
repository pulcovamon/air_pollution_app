import React from "react";

export default function Home() {
    return (
        <div className="home">
            <h3>Welcome to Air Quality Monitoring App</h3>
            <p>
                This application provides information about air quality in selected cities.
                You can find here charts with change of Air Quality Index (AQI) or amount of certain pollutant in one month.
                There is also order of selected cities according to AQI.
                Origin of data is <a href="https://openweathermap.org/api/air-pollution">Open Weather - Air Pollution API</a>.
            </p>
            <p>
                If you want, you can use API instead of this frontend:
                <a href="http://0.0.0.0:8000/docs">API</a>.
                There is also web documentation of this app:
                <a href="#">MKDocs</a>.
            </p>
            <p>
                This project was created as school semestral project for subject TBA at FBMI CTU.
            </p>
        </div>
    )
}