from pyrogram import Client, filters
from AM import AM
import time
import random
from config import BOT_USERNAME, CHANNEL, SUPPORT, OWNER_USERNAME, OWNER_ID
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

# ------------------------------------------------------------------------------- #

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
# ------------------------------------------------------------------------------- #
HELP_TEXT = """
ʜᴇʟʟᴏ {} 
\n⋆─────────────────────⋆
ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴀᴠᴀɪʟᴀʙʟᴇ  ᴄᴏᴍᴍᴀɴᴅs:

⦿ /play ➠ ᴘʟᴀʏs ᴀ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.
⦿ /vplay  ➠ ᴘʟᴀʏs ᴀ sᴏɴɢ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ.
⦿ /porn  ➠sᴏᴏɴ.
⦿ /stop ➠ sᴛᴏᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ sᴏɴɢ.
⦿ /end ➠ ᴇɴᴅs ᴛʜᴇ ᴍᴜsɪᴄ ᴘʟᴀʏʙᴀᴄᴋ.
⦿ /skip ➠ sᴋɪᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴏɴɢ.
⦿ /volume ➠ ᴀᴅᴊᴜsᴛs ᴛʜᴇ ᴠᴏʟᴜᴍᴇ ʟᴇᴠᴇʟ.
⦿ /song ➠ ᴅᴏᴡɴʟᴏᴀᴅ ғᴏʀ ᴀ sᴏɴɢ.
⦿ /video ➠ ᴅᴏᴡɴʟᴏᴀᴅ ғᴏʀ ᴀ ᴠɪᴅᴇᴏ.
⦿ /id ➠ ᴅɪsᴘʟᴀʏs ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ ᴏʀ ɢʀᴏᴜᴘ ɪᴅ.

"""

START_TEXT = """
ʜᴇʟʟᴏ {} 
\n⋆─────────────────────⋆
ᴍʏ ɴᴀᴍᴇ ɪꜱ 𝙀𝙘𝙤 \n⋆─────────────────────⋆
Iᴍᴍᴇʀsᴇ ʏᴏᴜʀsᴇʟғ ɪɴ ᴀ ᴡᴏʀʟᴅ ᴏғ ᴍᴜsɪᴄ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ\n⋆─────────────────────⋆
Dɪsᴄᴏᴠᴇʀ, ᴘʟᴀʏ, ᴀɴᴅ ᴇɴJᴏʏ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ ᴛᴜɴᴇs ʀɪɢʜᴛ ʜᴇʀᴇ\n⋆─────────────────────⋆
Sɪᴍᴘʟʏ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ sᴏɴɢ ᴏʀ ᴀʀᴛɪsᴛ, ᴀɴᴅ ʟᴇᴛ ᴛʜᴇ ᴍᴇʟᴏᴅʏ ʙᴇɢɪɴ. \n⋆─────────────────────⋆
Usᴇ Help ғᴏʀ ᴍᴏʀᴇ ᴄᴏᴍᴍᴀɴᴅs. 🎶
"""
# ------------------------------------------------------------------------------- #

button = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton("ᴅᴇᴠ", url=f"t.me/{OWNER_USERNAME}"),
    ],
    [
        InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ", callback_data="help_"),
    ]
])


@AM.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_photo(
        photo=random.choice(AM_PIC),
        caption=START_TEXT.format(message.from_user.mention, message.from_user.id),
        reply_markup=button
    )
@AM.on_callback_query(filters.regex("^help_"))
async def help_callback(_, query):
    await query.message.reply_photo(
        photo=random.choice(AM_PIC),
        caption=HELP_TEXT.format(query.from_user.mention, query.from_user.id)  # Fix: Use query instead of message
    )


@AM.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==OWNER_ID:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)

# ------------------------------------------------------------------------------- #




