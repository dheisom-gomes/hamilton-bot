from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.filters import command, group
from . import all, groups


def register(client: Client):
    client.add_handler(MessageHandler(all.start, command("start")))
