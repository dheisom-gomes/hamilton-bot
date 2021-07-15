from os import environ
from pyrogram import Client
from .database import Manager as DatabaseManager


app = Client(
    session_name=__name__,
    api_id=int(environ.get("TELEGRAM_API_ID")),
    api_hash=environ.get("TELEGRAM_API_HASH"),
    bot_token=environ.get("TELEGRAM_BOT_TOKEN")
)

database = DatabaseManager(
    url=environ.get("DATABASE_URL")
)
