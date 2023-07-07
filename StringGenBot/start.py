from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

"ᴡᴇʟᴄᴏᴍᴇ!!! ᴜꜱᴀɢᴇ ᴄᴍᴅꜱ ʟɪꜱᴛᴇᴅ ʙᴇʟʟᴏᴡ!!!/"
"ꜰɪʀꜱᴛ ᴏꜰ ᴀʟʟ ᴊᴏɪɴ ᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ ʟɪꜱᴛᴇᴅ ʙᴇʟᴏᴡ!!!/"
"ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴠɪꜱɪᴛɪɴɢ!!!"
"Mᴀᴅᴇ ʙʏ : [//ᴋᴀʀᴛɪᴋ ʟᴇɢᴇɴᴅ//](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ʙᴜʏ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅꜱ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("ꜱᴍᴍ ᴘᴀɴᴇʟ", url="https://realsmmpanel.online"),
                    InlineKeyboardButton("ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url="https://t.me/evonity")
                ],
                 [
                    InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/EvonixZone")
                ],
                 [
                    InlineKeyboardButton("ᴀᴅᴅ ꜰᴜɴᴅ", callback_data="funding"),
                    InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="help")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
