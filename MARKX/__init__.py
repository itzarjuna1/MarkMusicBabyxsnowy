import asyncio
from aiohttp import ClientSession

from MARKX.core.bot import MARKXBot
from MARKX.core.dir import dirr
from MARKX.core.git import git
from MARKX.core.userbot import Userbot
from MARKX.misc import dbb, heroku, sudo
from .logging import LOGGER

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
    # 1. Start aiohttp session
    await init_session()

    # 2. Run app setup routines
    dirr()
    git()
    dbb()
    heroku()
    sudo()

    # 3. Initialize Bot Clients
    global app, userbot
    app = MARKXBot()
    userbot = Userbot()

    # 4. Initialize API clients
    from .platforms import YouTubeAPI, CarbonAPI, SpotifyAPI, AppleAPI, RessoAPI, SoundAPI, TeleAPI
    global YouTube, Carbon, Spotify, Apple, Resso, SoundCloud, Telegram
    YouTube = YouTubeAPI()
    Carbon = CarbonAPI()
    Spotify = SpotifyAPI()
    Apple = AppleAPI()
    Resso = RessoAPI()
    SoundCloud = SoundAPI()
    Telegram = TeleAPI()

# Entry point
if __name__ == "__main__":
    try:
        asyncio.run(startup())
    except KeyboardInterrupt:
        pass
    finally:
        asyncio.run(close_session())
