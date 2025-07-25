import json
import os

from MARKX.core.bot import MARKXBot
from MARKX.core.dir import dirr
from MARKX.core.git import git
from MARKX.core.userbot import Userbot
from MARKX.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()

git()

dbb()

heroku()

sudo()

app = MARKXBot()

userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
