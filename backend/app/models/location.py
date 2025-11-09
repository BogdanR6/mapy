from typing import override
from app.services.ip_api import lookup_ip_coords
import logging

logger = logging.getLogger(__name__)

class Location:
    def __init__(self, ip: str, lat: float, lon: float, name: str | None = None):
        self.__ip = ip
        self.__lat = lat
        self.__lon = lon
        self.__name = name or "Unknown"

    @classmethod
    def from_ip(cls, ip: str, name: str | None = None) -> "Location":
        """Factory method that looks up coordinates for an IP."""
        try:
            lat, lon = lookup_ip_coords(ip)
            return cls(ip, lat, lon, name)
        except Exception as e:
            logger.warning(f"Error fetching IP info for {ip}: {e}")
            # return dummy coordinates if lookup fails
            return cls(ip=ip, lat=0.0, lon=0.0)

    @property
    def ip(self) -> str:
        return self.__ip

    @property
    def longitude(self) -> float:
        return self.__lon

    @property
    def latitude(self) -> float:
        return self.__lat

    @property
    def name(self) -> str:
        return self.__name

    @property
    def coordinates(self) -> tuple[float, float]:
        return (self.__lat, self.__lon)

    @override
    def __repr__(self) -> str:
        return f"Location(ip={self.__ip!r}, lat={self.__lat}, lon={self.__lon}, name={self.__name!r})"
