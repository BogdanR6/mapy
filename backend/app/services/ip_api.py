import requests
from typing import cast
from app.models.ip_api_response import IpApiResponse

def lookup_ip(ip: str) -> IpApiResponse:
    """Returns the api respose to the call to ip-api with the provided ip"""
    response = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
    return cast(IpApiResponse, response.json())

def lookup_ip_coords(ip: str) -> tuple[float, float]:
    """Returns the latitude and longitude corespunding to the provided ip"""
    data = lookup_ip(ip)
    return (
        float(data.get("lat", 0.0) or 0.0),
        float(data.get("lon", 0.0) or 0.0),
    )
