from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config



ask_ques = "**ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴘ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴠᴀɴ ʙᴜʏ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅꜱ ᴀɴᴅ ᴜꜱᴇ ꜱᴍᴍ ᴘᴀɴᴇʟ ʟɪꜱᴛᴇᴅ ɪɴ ʙᴜᴛᴛᴏɴ ꜰᴏʀ ꜱᴍᴍ ʀᴇᴀʟᴛᴇᴅ ꜱᴇʀᴠɪᴄᴇꜱ!**"
buttons_ques = [
    [
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ", callback_data="start"),
        InlineKeyboardButton("ꜱᴍᴍ ᴘᴀɴᴇʟ", callback_data="")
    ]
