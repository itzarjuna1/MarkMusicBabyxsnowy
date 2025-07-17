import asyncio
from aiohttp import ClientSession

from MARKX.core.bot import MARKXBot
from MARKX.core.dir import dirr
from MARKX.core.git import git
from MARKX.core.userbot import Userbot
from MARKX.misc import dbb, heroku, sudo
from .logging import LOGGER

# Declare these at module level so they can be imported safely
app = None
userbot = None

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

    # Initialize aiohttp session
    await init_session()

    # Run setup tasks
    dirr()
    git()
    dbb()
    heroku()
    sudo()

    # Create bot clients
    app = MARKXBot()
    userbot = Userbot()

    # Import and initialize API wrappers
    from .platforms import YouTubeAPI, CarbonAPI, SpotifyAPI, AppleAPI, RessoAPI, SoundAPI, TeleAPI

    global YouTube, Carbon, Spotify, Apple, Resso, SoundCloud, Telegram
    YouTube = YouTubeAPI()
    Carbon = CarbonAPI()
    Spotify = SpotifyAPI()
    Apple = AppleAPI()
    Resso = RessoAPI()
    SoundCloud = SoundAPI()
    Telegram = TeleAPI()

# Graceful shutdown helper
async def shutdown():
    await close_session()
