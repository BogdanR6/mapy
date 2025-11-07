class Map {
  constructor(center, zoom) {
    this.map = L.map('map').setView(center, zoom)
  }

  aplyTileLayer(urlTemplate, maxZoom, attribution) {
    L.tileLayer(urlTemplate, {
      maxZoom: maxZoom,
      attribution: attribution
    }).addTo(this.map);
  }

  addMarker(coordinates, popupText = null) {
    var marker = L.marker(coordinates).addTo(this.map)

    if (typeof popupText === 'string' || popupText instanceof String) {
      marker.bindPopup(popupText)
      marker.openPopup();
    }
  }
}

// Fetch helper
async function fetchJSON(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (err) {
    console.error("Fetch failed:", err);
    return null;
  }
}

async function main() {
  zoom = 13
  center = [51.505, -0.09]
  urlTemplate = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
  attribution = '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'

  var map = new Map(center, zoom)
  map.aplyTileLayer(urlTemplate, 13, attribution)

  // Fetch coordinates from backend
  const backendUrl = 'http://localhost:8000/api/locations';
  const locations = await fetchJSON(backendUrl);

  if (locations) {
    // Hello World Test
    console.log(locations)
    console.log(locations.message)
    map.addMarker(center, locations.message)
  }
}
main()
