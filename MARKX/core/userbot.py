import sys
from pyrogram import Client
from pyrogram.sessions import StringSession

import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot:
    def __init__(self):
        self.one = Client(
            StringSession(config.STRING1),
            config.API_ID,
            config.API_HASH,
            no_updates=True,
        ) if config.STRING1 else None

        self.two = Client(
            StringSession(config.STRING2),
            config.API_ID,
            config.API_HASH,
            no_updates=True,
        ) if config.STRING2 else None

        self.three = Client(
            StringSession(config.STRING3),
            config.API_ID,
            config.API_HASH,
            no_updates=True,
        ) if config.STRING3 else None

        self.four = Client(
            StringSession(config.STRING4),
            config.API_ID,
            config.API_HASH,
            no_updates=True,
        ) if config.STRING4 else None

        self.five = Client(
            StringSession(config.STRING5),
            config.API_ID,
            config.API_HASH,
            no_updates=True,
        ) if config.STRING5 else None