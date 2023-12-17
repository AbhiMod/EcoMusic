from pyrogram import filters, Client
from config import OWNER_ID
from AM import AM
import random
from AM.Helper.db import *
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

AM_PIC = [
    "https://telegra.ph/file/7c25ef427c9f3cded5577.jpg",
    "https://telegra.ph/file/625d235cc0a22fb8525b5.jpg",
    "https://telegra.ph/file/1c62254d59baf7f968ba7.jpg",
    "https://telegra.ph/file/7a0553bd4664486ab3008.jpg",
    "https://telegra.ph/file/7b4dfa606e6f23961d30e.jpg",
    "https://telegra.ph/file/2773dec98d87b8562618c.jpg",
    "https://telegra.ph/file/80353d02e0368b71d2666.jpg",
    "https://telegra.ph/file/6e5331dc4bef87464ea1c.jpg",
    "https://telegra.ph/file/199a2e44cb8e77bb21b34.jpg",
    "https://telegra.ph/file/8371bcd8952d089f9ec05.jpg",
    "https://telegra.ph/file/f970e559dd1bb96fced1a.jpg",
    "https://telegra.ph/file/59a305f8ce0c4e85949cc.jpg"
]


@AM.on_message(group=10)
async def chat_watcher_func(_, message):
    try:
        if message.from_user:
            us_in_db = await get_user(message.from_user.id)
            if not us_in_db:
                await add_user(message.from_user.id)

        chat_id = (message.chat.id if message.chat.id != message.from_user.id else None)

        if not chat_id:
            return

        in_db = await get_chat(chat_id)
        if not in_db:
            await add_chat(chat_id)
    except:
        pass
        


# --------------------------------------------------------------------------------- #


@AM.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(cli: Client, message: Message):
    users = len(await get_users())
    chats = len(await get_chats())
    await message.reply_photo(
        photo=random.choice(AM_PIC),
        caption=f"""**ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ** {(await cli.get_me()).mention} :

➻ ᴄʜᴀᴛs : {chats}
➻ ᴜsᴇʀs : {users}
"""
    )
    
# --------------------------------------------------------------------------------- #
