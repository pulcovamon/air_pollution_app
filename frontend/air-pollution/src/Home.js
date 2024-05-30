import React from "react";

export default function Home() {
    return (
        <div className="home">
            <h3>Welcome to Air Quality Monitoring App</h3>
            <p>
                This application provides information about air quality in selected cities.
                Origin of data is <a href="https://openweathermap.org/api/air-pollution">Open Weather - Air Pollution API</a>.
            </p>
        </div>
    )
}