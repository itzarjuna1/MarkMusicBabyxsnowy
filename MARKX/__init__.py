import asyncio
from aiohttp import ClientSession

from MARKX.core.bot import MARKXBot
from MARKX.core.dir import dirr
from MARKX.core.git import git
from MARKX.core.userbot import Userbot
from MARKX.misc import db, heroku, sudo
from .logging import LOGGER

# Declare globals at module level
app = None
userbot = None

# Declare API wrappers as None initially
YouTube = None
Carbon = None
Spotify = None
Apple = None
Resso = None
SoundCloud = None
Telegram = None

aiohttpsession = None

async def init_session():
    global aiohttpsession
    aiohttpsession = ClientSession()

async def close_session():
    global aiohttpsession
    if aiohttpsession:
        await aiohttpsession.close()

async def startup():
    global app, userbot
    global YouTube, Carbon, Spotify, Apple, Resso, SoundCloud, Telegram

    await init_session()

    dirr()
    git()
    db()
    heroku()
    sudo()

    app = MARKXBot()
    userbot = Userbot()

    from .platforms import YouTubeAPI, CarbonAPI, SpotifyAPI, AppleAPI, RessoAPI, SoundAPI, TeleAPI

    YouTube = YouTubeAPI()
    Carbon = CarbonAPI()
    Spotify = SpotifyAPI()
    Apple = AppleAPI()
    Resso = RessoAPI()
    SoundCloud = SoundAPI()
    Telegram = TeleAPI()

async def shutdown():
    await close_session()
