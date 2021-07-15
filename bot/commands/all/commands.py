from pyrogram.types import Message
from typing import Any


async def start(_: Any, message: Message):
    await message.reply(
        "Olá, sou um bot de administrar grupos e estou em desenvolvimento!"
    )
