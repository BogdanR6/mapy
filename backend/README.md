# Mapy Backend
The Mapy backend is written in Python using the *_fastapi_* framework.

## Run it inside Docker
### Prerequisites
- Docker

### Setup and Run
```bash
# create image
$ docker build -t mapy-backend .
# run the container
$ docker run -d --name mapy-backend -p 8000:8000 mapy-backend
# now the backend can be accessed at http://localhost:8000/

# when you are done the container can be stopped with
$ docker stop mapy-backend
```

## For Development
### Prerequisites
- Python 3.10+

### Setup and Run
```bash
# create the python venv
$ python -m venv .venv
# activate the python venv
$ source .venv/bin/activate
# install the requierments
$ pip install -r requirements.txt
# run the backend
$ fastapi dev main.py
```
