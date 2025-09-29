import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function PortScanChart() {
  const [scanData, setScanData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/scans')
      .then(res => res.json())
      .then(data => setScanData(data?.results || null));
  }, []);

  if (!scanData) return <div>Chargement...</div>;

  const hosts = Object.keys(scanData);
  const portCounts = hosts.map(host => scanData[host].length);

  const chartData = {
    labels: hosts,
    datasets: [
      {
        label: 'Ports ouverts par hôte',
        data: portCounts,
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      },
    ],
  };

  return (
    <div>
      <h2>Ports ouverts sur le réseau</h2>
      <Bar
        data={chartData}
        options={
          responsive: true,
          plugins: { legend: { position: 'top' } },
        }
      />
      <pre>{JSON.stringify(scanData, null, 2)}</pre>
    </div>
  );
}

export default PortScanChart;