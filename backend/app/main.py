from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Only add CORS middleware in development
APP_ENV = os.getenv("APP_ENV", "development")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:8080")

if APP_ENV == "development":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[FRONTEND_URL],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/")
def root():
    return {"message" : "Server Running"}

@app.get("/connect")
def record_connection(request: Request) -> dict[str, float | str | None]:
    if os.getenv("APP_ENV") == "development":
        ip = "8.8.8.8"
    else:
        ip = request.client.host

    data = requests.get(f"http://ip-api.com/json/{ip}").json()
    lat, lon = data.get("lat"), data.get("lon")
    return {"ip": ip, "lat": lat, "lon": lon}

@app.get("/points")
def get_points():
    # Should read from database
    pass
