import asyncio
from pyrogram import Client
from pyrogram.sessions import StringSession
from config import STRING_SESSION, API_ID, API_HASH

Userbot = None

if STRING_SESSION:
    print("[INFO] Starting Userbot Session...")

    try:
        Userbot = Client(
            name="Userbot",
            session_string=StringSession(STRING_SESSION),
            api_id=API_ID,
            api_hash=API_HASH
        )

        asyncio.get_event_loop().run_until_complete(Userbot.start())
        me = asyncio.get_event_loop().run_until_complete(Userbot.get_me())
        print(f"[USERBOT] Started as {me.first_name} (ID: {me.id})")

    except Exception as e:
        print(f"[ERROR] Failed to start userbot: {e}")
        Userbot = None

else:
    print("[INFO] No STRING_SESSION provided. Skipping userbot startup.")