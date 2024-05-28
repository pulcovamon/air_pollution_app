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
        data: data.map(entry => entry.value),
        borderColor: 'rgba(50,150,150,1)',
        backgroundColor: 'rgba(50,150,150,0.2)',
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      title: {
        display: true,
        text: title,
        font: {
          size: 20,
        },
        color: 'white',
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
          color: 'white',
          font: {
            size: 12,
          },
        },
      },
      y: {
        ticks: {
          display: true,
          color: 'white',
          font: {
            size: 12,
          },
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
