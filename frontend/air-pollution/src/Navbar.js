import React from "react";
import AQI from "./AQI";
import Parameters from "./Parameters";

export default function Navbar({ handleSelection }) {
  return (
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
  );
}
   