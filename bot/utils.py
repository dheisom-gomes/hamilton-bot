from pyrogram import Client
from pyrogram.types import Message


async def isAdmin(client: Client, message: Message) -> bool:
    admin_list = await client.get_chat_members(
        chat_id=message.chat.id,
        filter="administrators"
    )
    async for admin in admin_list:
        if admin.user.id == message.from_user.id:
            return True
    return False
