async function connectToBackend() {
  try {
    const backendUrl = CONFIG.BACKEND_URL;
    const response = await fetch(`${backendUrl}/locations/connect`);
    const location = await response.json();
    console.log('Connected:', location);
    return location;
  } catch (err) {
    console.error('Connection failed:', err);
    return null;
  }
}

async function main() {
  const zoom = 13
  const urlTemplate = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
  const attribution = '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'

  // connect to database
  const location = await connectToBackend()

  if (!location) {
    return
  }

  // create the map and add the location determined by the ip
  console.log("Creating map...")
  coordinates = [location.lat, location.lon]
  var map = new Map(coordinates, zoom)
  map.aplyTileLayer(urlTemplate, 13, attribution)
  console.log("Map created")

  console.log("Marking user location...")
  map.addMarker(coordinates, location.name)
  console.log("User location marked")

  // ask the user to store the location
  console.log("Asking user consent...")
  showConsentPopup();
  console.log("Finished main function")
}
main()
