const plantSelect = document.getElementById('plantSelect');
const plantDetails = document.getElementById('plantDetails');
const addPlantBtn = document.getElementById('addPlantBtn');
const tabs = document.querySelectorAll('.tab-button');
const tabContents = document.querySelectorAll('.tab-content');
const recordItemTemplate = document.getElementById('recordItemTemplate');

let plants = [];
let selectedPlantId = null;

async function fetchPlants() {
  const response = await fetch('/api/plants');
  plants = await response.json();
  renderPlantOptions();
}

function renderPlantOptions() {
  plantSelect.innerHTML = '';
  plants.forEach(plant => {
    const option = document.createElement('option');
    option.value = plant.id;
    option.textContent = `${plant.name} (${plant.location})`;
    plantSelect.appendChild(option);
  });

  if (plants.length > 0) {
    selectedPlantId = selectedPlantId || plants[0].id;
    plantSelect.value = selectedPlantId;
  }

  renderSelectedPlant();
}

function renderSelectedPlant() {
  const plant = plants.find(p => p.id === selectedPlantId);
  if (!plant) {
    plantDetails.innerHTML = '<p>Please add a plant to get started.</p>';
    tabContents.forEach(content => (content.innerHTML = ''));
    return;
  }

  plantDetails.innerHTML = `
    <h3>${plant.name}</h3>
    <p><strong>Location:</strong> ${plant.location}</p>
  `;

  renderRecords('downtime', plant.downtime);
  renderRecords('breakdowns', plant.breakdowns);
  renderRecords('spares', plant.spares);
  renderRecords('observations', plant.observations);
}

function renderRecords(type, records) {
  const container = document.getElementById(`${type}Tab`);
  const title = type.charAt(0).toUpperCase() + type.slice(1);
  container.innerHTML = `
    <div class="record-list"></div>
    <div class="form-block">
      <h3>Add ${title}</h3>
      <form id="${type}Form">
        <label>Note</label>
        <textarea name="note" rows="2" required></textarea>
        ${type === 'downtime' ? '<div class="row"><div><label>Duration</label><input name="duration" required /></div></div>' : ''}
        ${type === 'breakdowns' ? '<div class="row"><div><label>System</label><input name="system" required /></div></div>' : ''}
        ${type === 'spares' ? '<div class="row"><div><label>Part Number</label><input name="partNumber" required /></div><div><label>Priority</label><select name="priority"><option>Normal</option><option>High</option><option>Urgent</option></select></div></div>' : ''}
        ${type === 'observations' ? '<div class="row"><div><label>Severity</label><select name="severity"><option>Normal</option><option>Medium</option><option>High</option></select></div></div>' : ''}
        <button type="submit">Save</button>
      </form>
    </div>
  `;

  const list = container.querySelector('.record-list');
  if (records.length === 0) {
    list.innerHTML = '<p>No records yet.</p>';
  } else {
    records.forEach(record => {
      const item = recordItemTemplate.content.cloneNode(true);
      item.querySelector('.record-note').textContent = record.note;
      item.querySelector('.record-meta').textContent = `Created: ${new Date(record.createdAt).toLocaleString()}`;
      item.querySelector('.record-extra').textContent = formatRecordExtra(type, record);
      list.appendChild(item);
    });
  }

  const form = document.getElementById(`${type}Form`);
  form.addEventListener('submit', async event => {
    event.preventDefault();
    const formData = new FormData(form);
    const payload = {
      type: type.slice(0, -1),
      note: formData.get('note'),
      duration: formData.get('duration'),
      system: formData.get('system'),
      partNumber: formData.get('partNumber'),
      priority: formData.get('priority'),
      severity: formData.get('severity')
    };

    await fetch(`/api/plants/${selectedPlantId}/records`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    form.reset();
    await fetchPlants();
  });
}

function formatRecordExtra(type, record) {
  switch (type) {
    case 'downtime':
      return `Duration: ${record.duration || 'N/A'}`;
    case 'breakdowns':
      return `System: ${record.system || 'N/A'}`;
    case 'spares':
      return `Part: ${record.partNumber || 'N/A'} · Priority: ${record.priority}`;
    case 'observations':
      return `Severity: ${record.severity}`;
    default:
      return '';
  }
}

addPlantBtn.addEventListener('click', async () => {
  const name = prompt('Plant name');
  if (!name) return;
  const location = prompt('Plant location');

  await fetch('/api/plants', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, location })
  });

  await fetchPlants();
});

plantSelect.addEventListener('change', () => {
  selectedPlantId = plantSelect.value;
  renderSelectedPlant();
});

tabs.forEach(button => {
  button.addEventListener('click', () => {
    tabs.forEach(btn => btn.classList.remove('active'));
    tabContents.forEach(tab => tab.classList.remove('active'));
    button.classList.add('active');
    document.getElementById(`${button.dataset.tab}Tab`).classList.add('active');
  });
});

fetchPlants();
