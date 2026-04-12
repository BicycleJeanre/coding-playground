const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const port = process.env.PORT || 3000;
const dataFile = path.join(__dirname, 'data', 'sample-data.json');

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

function loadData() {
  try {
    const raw = fs.readFileSync(dataFile, 'utf8');
    return JSON.parse(raw);
  } catch (error) {
    console.error('Failed to load data:', error);
    return { plants: [] };
  }
}

function saveData(data) {
  try {
    fs.writeFileSync(dataFile, JSON.stringify(data, null, 2), 'utf8');
  } catch (error) {
    console.error('Failed to save data:', error);
  }
}

app.get('/api/plants', (req, res) => {
  const data = loadData();
  res.json(data.plants);
});

app.post('/api/plants', (req, res) => {
  const data = loadData();
  const plant = {
    id: Date.now().toString(),
    name: req.body.name || 'New Plant',
    location: req.body.location || '',
    downtime: [],
    breakdowns: [],
    spares: [],
    observations: []
  };
  data.plants.push(plant);
  saveData(data);
  res.json(plant);
});

app.post('/api/plants/:plantId/records', (req, res) => {
  const data = loadData();
  const plant = data.plants.find(p => p.id === req.params.plantId);
  if (!plant) {
    return res.status(404).json({ error: 'Plant not found' });
  }

  const record = {
    id: Date.now().toString(),
    createdAt: new Date().toISOString(),
    note: req.body.note || '',
    details: req.body.details || {}
  };

  switch (req.body.type) {
    case 'downtime':
      record.duration = req.body.duration || '';
      plant.downtime.push(record);
      break;
    case 'breakdown':
      record.system = req.body.system || '';
      plant.breakdowns.push(record);
      break;
    case 'spare':
      record.partNumber = req.body.partNumber || '';
      record.priority = req.body.priority || 'Normal';
      plant.spares.push(record);
      break;
    case 'observation':
      record.severity = req.body.severity || 'Normal';
      plant.observations.push(record);
      break;
    default:
      return res.status(400).json({ error: 'Invalid record type' });
  }

  saveData(data);
  res.json(record);
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
  console.log(`Downtime tracker app listening at http://localhost:${port}`);
});
