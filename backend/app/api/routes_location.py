import os
from fastapi import APIRouter, Request
from app.models.location import Location
from app.repositories.location_repository import save_location, get_all_locations

router = APIRouter(prefix="/locations", tags=["locations"])

@router.get("/connect")
def record_connection(request: Request) -> dict[str, float | str | None]:
    if os.getenv("APP_ENV") == "development":
        ip = "8.8.8.8"
    else:
        ip = request.client.host

    user_name = "Sam" # TODO: get from frontend

    location = Location.from_ip(ip, user_name)

    should_save_location = True  # TODO: get from frontend
    if should_save_location:
        save_location(location)

    return {"ip": location.ip, "lat": location.latitude, "lon": location.longitude, "name": location.name}

@router.get("/points")
def get_points():
    return get_all_locations()
