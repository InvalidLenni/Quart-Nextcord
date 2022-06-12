from .exceptions import *
from .utils import *

from .client import DiscordOAuth2Session


__all__ = [
    "DiscordOAuth2Session",
    "requires_authorization",
    "HttpException",
    "RateLimited",
    "Unauthorized",
    "AccessDenied",
]


__version__ = "2.1.6a1"
__name__ = "Quart-Nextcord"
__release__ = "2.1.6a1"