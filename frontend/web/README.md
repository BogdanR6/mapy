# Mapy Web Frontend
The Mapy web frontend is just _html_+_css_+_js_ using the _Leaflet_ JS library to display
the world map.

## Run it inside Docker
### Prerequisites
- Docker

### Run the frontend
```bash
# create the image
$ docker build -t mapy-web-frontend .
# create the container
$ docker run -d --name mapy-web-frontend -p 8080:80 mapy-web-frontend
# now the frontend is available at http://localhost:8080

# to stop the container
$ docker stop mapy-web-frontend
```

## For Development
### Prerequisites
- live-server (install using _nmp_)

### Run the frontend
```bash
# just start live server
# it will open in browser and reload on file changes
$ live-server
```
