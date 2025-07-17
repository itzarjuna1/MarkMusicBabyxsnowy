import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", 24880308))
API_HASH = getenv("API_HASH", fce3dc86e231613c5e0e164cdf8f1ca9)
BOT_TOKEN = getenv("BOT_TOKEN", "7597057529:AAEOEhIY2vAAeWyJNLapAc0sDLHo9Az7wmY")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "90"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002643544937"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "snowyxmusic")

OWNER_ID = list(map(int, getenv("OWNER_ID", "7926944005").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Marrk-85/MarkMusic"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/dark_x_knight_musiczz_support"
)
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/+5CjEKZLxJlU3OGU1"
)

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://telegra.ph/file/f84d28d91512a445ecce1.mp4")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

STRING1 = getenv("STRING_SESSION", "AQF7pLQAojetQZtb9UXJs4lyP3JPmWAk-kFniZR4cciu1Lh5svG19MFQ0uZjSxH0HwLQczOgfc-CZn_TAdjEQTOUp7wumUntlr7GdPFTyL5IT7oI0pExGSgu8cXb9UJ6lozm12nW3jjQ7kfP4IZJPLtzbZ5fp0Qc8Z72k09EavrM_nmddtYjXsETOxBez2j3IC6kiFHQ2jQB3RvhTFvi6cVSXytwU_pXEk2rb8WqwttXEJUp5ar4ZOSgplWfI7AY1xpM-FLTUTgjAO3ddPCF8ii9OSBfmz4Dr-pX26x8bQt_7CMqcyUZnnD7o6-xXRy2AJoM2pUAOLlVgpryPSsdVhQ5hMkMIQAAAAHoG-_JAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "anonxlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/a5c1e69220a8913c4c271-ca24b2f904e8ab971c.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/c8901d533e9862c400c2f-18494dd325b69d564e.jpg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "assets/Playlist.jpeg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL", "assets/Global.jpeg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://graph.org/file/e7cb57277bd4269af94e1-86e9e21ae1a937c915.jpg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "assets/Audio.jpeg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "assets/Video.jpeg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "assets/Stream.jpeg")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "assets/Soundcloud.jpeg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "assets/Youtube.jpeg")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "assets/SpotifyArtist.jpeg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "assets/SpotifyAlbum.jpeg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "assets/SpotifyPlaylist.jpeg")

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1] if "me/" in SUPPORT_GROUP else SUPPORT_GROUP

# URL Checks
def validate_url(name, url, default_asset):
    if url and url != default_asset:
        if not re.match("(?:http|https)://", url):
            print(f"[ERROR] - Your {name} url is wrong. Please ensure that it starts with https://")
            sys.exit()

validate_url("UPSTREAM_REPO", UPSTREAM_REPO, "")
validate_url("PING_IMG_URL", PING_IMG_URL, "assets/Ping.jpeg")
validate_url("PLAYLIST_IMG_URL", PLAYLIST_IMG_URL, "assets/Playlist.jpeg")
validate_url("GLOBAL_IMG_URL", GLOBAL_IMG_URL, "assets/Global.jpeg")
validate_url("STATS_IMG_URL", STATS_IMG_URL, "assets/Stats.jpeg")
validate_url("TELEGRAM_AUDIO_URL", TELEGRAM_AUDIO_URL, "assets/Audio.jpeg")
validate_url("TELEGRAM_VIDEO_URL", TELEGRAM_VIDEO_URL, "assets/Video.jpeg")
validate_url("STREAM_IMG_URL", STREAM_IMG_URL, "assets/Stream.jpeg")
validate_url("SOUNCLOUD_IMG_URL", SOUNCLOUD_IMG_URL, "assets/Soundcloud.jpeg")
validate_url("YOUTUBE_IMG_URL", YOUTUBE_IMG_URL, "assets/Youtube.jpeg")
