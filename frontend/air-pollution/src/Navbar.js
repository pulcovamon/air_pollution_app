import React from "react";

export default function Navbar({ handleSelection }) {
  return (
    <div className="navbar">
      <ul>
        <li>
            Air Quality Monitoring
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
      </ul>
    </div>
  );
}

   