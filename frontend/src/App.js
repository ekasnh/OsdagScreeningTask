import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { PrismViewer } from './PrismViewer';
import './App.css';

function App() {
  const [prisms, setPrisms] = useState([]);
  const [selectedPrism, setSelectedPrism] = useState(null);
  const [surfaceArea, setSurfaceArea] = useState(0);
  const [volume, setVolume] = useState(0);

  useEffect(() => {
    axios.get('/api/prisms/')
      .then(response => setPrisms(response.data))
      .catch(error => console.error('There was an error fetching the prism data!', error));
  }, []);

  const handlePrismSelect = (designation) => {
    const prism = prisms.find(p => p.designation === designation);
    setSelectedPrism(prism);
    axios.get(`/api/prisms/${prism.id}/calculate/`)
      .then(response => {
        setSurfaceArea(response.data.surface_area);
        setVolume(response.data.volume);
      })
      .catch(error => console.error('There was an error calculating the prism data!', error));
  };

  return (
    <div className="App">
      <h1>Rectangular Prism Viewer</h1>
      <select onChange={(e) => handlePrismSelect(e.target.value)}>
        <option value="">Select a prism</option>
        {prisms.map(prism => (
          <option key={prism.id} value={prism.designation}>
            {prism.designation}
          </option>
        ))}
      </select>
      {selectedPrism && (
        <div>
          <p>Surface Area: {surfaceArea}</p>
          <p>Volume: {volume}</p>
          <PrismViewer prism={selectedPrism} />
        </div>
      )}
    </div>
  );
}

export default App;
