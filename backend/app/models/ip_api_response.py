from typing import TypedDict

class IpApiResponse(TypedDict, total=False):
    """
    Response schema for ip-api.com JSON API.

    Full docs: https://ip-api.com/docs/api:json
    """
    query: str
    status: str
    country: str
    countryCode: str
    region: str
    regionName: str
    city: str
    zip: str
    lat: float
    lon: float
    timezone: str
    isp: str
    org: str
