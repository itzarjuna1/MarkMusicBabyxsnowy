import asyncio
from aiohttp import ClientSession

from MARKX.core.bot import MARKXBot
from MARKX.core.dir import dirr
from MARKX.core.git import git
from MARKX.core.userbot import Userbot
from MARKX.misc import dbb, heroku, sudo
from .logging import LOGGER

# Globals for bot clients
app = None
userbot = None

# Globals for APIs
YouTube = None
Carbon = None
Spotify = None
Apple = None
Resso = None
SoundCloud = None
Telegram = None

# Global aiohttp session
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

    # Init HTTP session
    await init_session()

    # Setup tasks
    dirr()
    git()
    dbb()
    heroku()
    sudo()

    # Initialize bot clients
    app = MARKXBot()
    userbot = Userbot()

    # Import and initialize API wrappers
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
