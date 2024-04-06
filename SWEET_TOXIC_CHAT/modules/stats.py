from pyrogram import filters, Client
from pyrogram.types import Message

from SWEET_TOXIC_CHAT import OWNER, SWEET_TOXIC_CHAT
from SWEET_TOXIC_CHAT.database.chats import get_served_chats
from SWEET_TOXIC_CHAT.database.users import get_served_users


@SWEET_TOXIC_CHAT.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {(await cli.get_me()).mention} :

➻ **ᴄʜᴀᴛs :** {chats}
➻ **ᴜsᴇʀs :** {users}"""
    )
