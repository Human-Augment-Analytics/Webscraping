'use client'
import React, {useEffect, useState} from 'react';
import Plot from 'react-plotly.js';

const MapComponent = () => {
    const [plotData, setPlotData] = useState(null);

    const fetchMapConfig = () => {
    const token = localStorage.getItem('token');

    // fetch('http://localhost:8000/map-config', {
    fetch('https://haaggtbe-production.up.railway.app/map-config', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(response => response.json())
      .then(data => setPlotData(data))
      .catch(error => console.error('Error fetching map config:', error));
  };

    useEffect(() => {
        fetchMapConfig();
    }, []);

    if (!plotData) {
        return <div>Loading...</div>;
    }

    return (
        <div className="w-full min-h-screen">
            <div className='h-16'/>
            <Plot
                className="w-full"
                style={{ minHeight: 'calc(100vh - 64px)' }}
                data={plotData.data}
                layout={plotData.layout}
                config={plotData.config}
            />
        </div>
    );
};

export default MapComponent;
