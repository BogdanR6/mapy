import os
from fastapi import APIRouter, Request
from app.models.consent_request import ConsentRequest
from app.models.location import Location
from app.repositories.location_repository import save_location, get_all_locations

def get_ip_from_request(request: Request) -> str:
    """ 
        Helper function to return the ip from a provided request.
        Returns a testing IP when the backend runs in development mode.
    """
    if os.getenv("APP_ENV") == "development":
        return "9.9.9.9"

    return request.client.host

router = APIRouter(prefix="/locations", tags=["locations"])

@router.get("/connect")
def record_connection(request: Request) -> dict[str, float | str | None]:
    """ Return the latitude and longitude corresponding to the requests ip. """
    ip = get_ip_from_request(request)

    location = Location.from_ip(ip)

    return {"lat": location.latitude, "lon": location.longitude}


@router.get("/points")
def get_points():
    """ Return all the points stored in the database. """
    return get_all_locations()


@router.post("/save")
async def save(payload: ConsentRequest, request: Request):
    """ Save the user data in the repository. """
    ip = get_ip_from_request(request)

    if payload.shouldSave:
        location = Location.from_ip(ip, payload.name)
        save_location(location)
        return {"message": "Location saved", "ip": ip}
    else:
        return {"message": "Location not saved"}
