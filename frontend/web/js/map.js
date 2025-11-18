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
