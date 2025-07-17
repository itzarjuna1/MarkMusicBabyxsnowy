import sys
from pyrogram import Client
from pyrogram.sessions import StringSession
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.one = Client(
            session_name=StringSession(config.STRING1),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        ) if config.STRING1 else None

        self.two = Client(
            session_name=StringSession(config.STRING2),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        ) if config.STRING2 else None

        self.three = Client(
            session_name=StringSession(config.STRING3),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        ) if config.STRING3 else None

        self.four = Client(
            session_name=StringSession(config.STRING4),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        ) if config.STRING4 else None

        self.five = Client(
            session_name=StringSession(config.STRING5),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        ) if config.STRING5 else None