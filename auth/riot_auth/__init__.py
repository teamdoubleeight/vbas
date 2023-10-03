# © 2023 VBASPY by Doubleeight with MIT License
# Riot auth part by Huba Tuba (floxay)

__version__ = "2.0"

from .auth import (
    RiotAuth,
    AuthenticationError,
    RiotAuthError,
    MultiFactorError,
    LimitRateError,
    UnknwonError,
    ResponsiveError,
)


__all__ = (
    "RiotAuth",
    "AuthenticationError",
    "RiotAuthError",
    "MultiFactorError",
    "LimitRateError",
    "UnknwonError",
    "ResponsiveError",
)
