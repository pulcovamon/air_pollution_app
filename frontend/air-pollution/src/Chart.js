import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export default function Chart({ data = [], title = "Chart" }) {
  // Check if data is empty
  if (!data.length) {
    return <div>No data available</div>;
  }

  const chartData = {
    labels: data.map(entry => new Date(entry.date).toLocaleDateString()),
    datasets: [
      {
        label: title,
        data: data.map(entry => entry.value),
        borderColor: 'rgba(75,192,192,1)',
        backgroundColor: 'rgba(75,192,192,0.2)',
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: title,
      },
    },
    layout: {
      padding: {
        left: 10,
        right: 10,
        top: 10,
        bottom: 10,
      },
    },
    scales: {
      x: {
        ticks: {
          display: true,
        },
      },
      y: {
        ticks: {
          display: true,
        },
      },
    },
  };

  return (
    <div style={{ width: '100%', height: '400px', margin: 'auto' }}>
      <Line data={chartData} options={options} />
    </div>
  );
}
