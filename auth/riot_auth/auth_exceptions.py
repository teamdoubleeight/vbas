# © 2023 VBASPY by Doubleeight with MIT License
# Riot auth part by Huba Tuba (floxay)

__all__ = (
    "RiotAuthenticationError",
    "RiotAuthError",
    "RiotMultifactorError",
    "RiotRatelimitError",
    "RiotUnknownErrorTypeError",
    "RiotUnknownResponseTypeError",
)


class RiotAuthError(Exception):
    """Base class for RiotAuth errors."""


class AuthenticationError(RiotAuthError):
    """Failed to Authenticate."""


class LimitRateError(RiotAuthError):
    """Rate limit error."""


class MultiFactorError(RiotAuthError):
    """2FA need to complete."""


class ResponsiveError(RiotAuthError):
    """Response type is unknwon."""


class UnknwonError(RiotAuthError):
    """Error type is unknwon."""
