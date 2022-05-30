# Quart-Nextcord
[![PyPI](https://img.shields.io/pypi/v/Quart-Nextcord?style=for-the-badge)](https://pypi.org/project/Quart-Nextcord/) [![Read the Docs](https://img.shields.io/readthedocs/quart-nextcord?style=for-the-badge)](https://quart-nextcord.readthedocs.io/en/latest/) 

Discord OAuth2 extension for Quart.


### Installation
To install current latest release you can use following command:
```sh
python3 -m pip install Quart-Nextcord
```


### Basic Example

```python
from quart import Quart, redirect, url_for
from quart_nextcord import DiscordOAuth2Session, requires_authorization, Unauthorized

app = Quart(__name__)

app.secret_key = b"random bytes representing quart secret key"

app.config["DISCORD_CLIENT_ID"] = 490732332240863233  # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = ""  # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = ""  # URL to your callback endpoint.
app.config["DISCORD_BOT_TOKEN"] = ""  # Required to access BOT resources.

nextcord = DiscordOAuth2Session(app)


@app.route("/login/")
async def login():
    return await nextcord.create_session()


@app.route("/callback/")
async def callback():
    await nextcord.callback()
    return redirect(url_for(".me"))


@app.errorhandler(Unauthorized)
async def redirect_unauthorized(e):
    return redirect(url_for("login"))


@app.route("/me/")
@requires_authorization
async def me():
    user = await nextcord.fetch_user()
    return f"""
    <html>
        <head>
            <title>{user.name}</title>
        </head>
        <body>
            <img src='{user.avatar_url}' />
        </body>
    </html>"""


if __name__ == "__main__":
    app.run()
```

For an example to the working application, check [`test_app.py`](tests/test_app.py)


### Requirements
* Quart
* Async-OAuthlib
* cachetools
* nextcord


### Documentation
Head over to [documentation] for full API reference. 


[documentation]: https://quart-nextcord.readthedocs.io/en/latest/
