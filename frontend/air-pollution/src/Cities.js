import React from 'react';

export default function CitySelect({ handleSelection, cities }) {
  return (
    <select onChange={handleSelection}>
      {cities.map(city => (
        <option key={city.id} value={city.id}>{city.name}</option>
      ))}
    </select>
  );
}
