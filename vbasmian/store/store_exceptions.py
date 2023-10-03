# © 2023 VBASPY by Doubleeight with MIT License

__all__ = (
    "EntTokenInvalidError",
    "RegionInvalidError",
    "RequestError",
)


class EntTokenInvalidError(Exception):
    """Bearer token or Entitlements token is invalid."""

class RegionInvalidError(Exception):
    """Bearer token or Entitlements token is invalid."""
    
class RequestError(Exception):
    """PUUID/Auth Token is invalid or unknwon error happened."""
