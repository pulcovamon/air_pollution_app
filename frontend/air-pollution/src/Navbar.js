import React from "react";

export default function Navbar({ handleSelection }) {
  return (
    <div className="navbar">
      <ul>
        <li>
        <button onClick={() => handleSelection("home")}>
            Air Quality Monitoring
          </button>
        </li>
        <li>
          <button onClick={() => handleSelection("AQI")}>
            Air Quality Index
          </button>
        </li>
        <li>
          <button onClick={() => handleSelection("Parameters")}>
            Air Quality Parameters
          </button>
        </li>
        <li>
          <button onClick={() => handleSelection("Statistics")}>
            Statistics
          </button>
        </li>
      </ul>
    </div>
  );
}

   