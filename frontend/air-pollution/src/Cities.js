import React from 'react';

export default function CitySelect({ cities, handleSelection }) {
    return (
        <div>
            <select onChange={(e) => handleSelection(e)}>
                {cities.map((city) => (
                <option key={city.id} value={city.id}>{city.name}</option>
                ))}
            </select>
        </div>
    )
}