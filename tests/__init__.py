import os

from quart import Quart
from quart_nextcord import DiscordOAuth2Session


def get_app():
    app = Quart(__name__)

    app.secret_key = b"%\xe0'\x01\xdeH\x8e\x85m|\xb3\xffCN\xc9g"
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "false"  # !! Only in development environment.

    app.config["DISCORD_CLIENT_ID"] = 815979836115517461
    app.config["DISCORD_CLIENT_SECRET"] = os.getenv("DISCORD_CLIENT_SECRET")
    app.config["DISCORD_BOT_TOKEN"] = os.getenv("DISCORD_BOT_TOKEN")
    app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"

    app.nextcord = DiscordOAuth2Session(app, client_id=815979836115517461)

    return app
