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
  const zoom = 13
  const urlTemplate = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
  const attribution = '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'

  // Fetch coordinates from backend
  const backendUrl = CONFIG.BACKEND_URL;
  const location = await fetchJSON(`${backendUrl}/connect`);

  if (location) {
    console.log(location)
    markerCoordinates = [location.lat, location.lon]
    var map = new Map(markerCoordinates, zoom)
    map.aplyTileLayer(urlTemplate, 13, attribution)

    map.addMarker(markerCoordinates)
  } else {
    console.log(location)
    console.log("Could not connect to server!")
    // TODO: Add a could not connect to server page
  }
}
main()
