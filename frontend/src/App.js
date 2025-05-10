import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';
import Select from 'react-select';
import './styles.css';

const App = () => {
  const [data, setData] = useState([]);
  const [selectedType, setSelectedType] = useState(null);
  const [selectedSeverity, setSelectedSeverity] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/api/pulses')
      .then(res => setData(res.data))
      .catch(err => console.error(err));
  }, []);

  // Filter logic
  const filteredData = data.filter(pulse => {
    const typeMatch = selectedType ? 
      pulse.indicators.some(ind => ind.type === selectedType.value) : true;
    const severityMatch = selectedSeverity ? 
      pulse.severity === selectedSeverity.value : true;
    return typeMatch && severityMatch;
  });

  // Chart configuration
  const chartData = {
    labels: filteredData.map(pulse => pulse.name),
    datasets: [{
      label: 'Number of Indicators',
      data: filteredData.map(pulse => pulse.indicators.length),
      backgroundColor: '#4CAF50',
    }]
  };

  // Filter options
  const typeOptions = [
    { value: 'IPv4', label: 'IPv4' },
    { value: 'domain', label: 'Domain' },
    { value: 'url', label: 'URL' }
  ];

  const severityOptions = [
    { value: 'red', label: 'Red' },
    { value: 'amber', label: 'Amber' },
    { value: 'green', label: 'Green' }
  ];

  return (
    <div className="container">
      <h1>CTI Dashboard</h1>
      
      <div className="filters">
        <Select
          options={typeOptions}
          placeholder="Filter by Indicator Type"
          onChange={setSelectedType}
          isClearable
        />
        <Select
          options={severityOptions}
          placeholder="Filter by Severity"
          onChange={setSelectedSeverity}
          isClearable
        />
      </div>

      <div className="chart-container">
        <Bar 
          data={chartData} 
          options={{ responsive: true, maintainAspectRatio: false }}
        />
      </div>

      <div className="threat-list">
        <h2>Threat Indicators</h2>
        <table>
          <thead>
            <tr>
              <th>Threat Name</th>
              <th>Indicators</th>
              <th>Severity</th>
            </tr>
          </thead>
          <tbody>
            {filteredData.map(pulse => (
              <tr key={pulse.id}>
                <td>{pulse.name}</td>
                <td>
                  <ul>
                    {pulse.indicators.map((ind, idx) => (
                      <li key={idx}>{ind.value} ({ind.type})</li>
                    ))}
                  </ul>
                </td>
                <td>
                  <span className={`severity-${pulse.severity}`}>
                    {pulse.severity}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default App;
