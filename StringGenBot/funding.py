from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("addfund"))
async def start(bot: Client, msg: Message):
    await bot.send_message(
        chat_id=msg.chat.id,
      api_id_msg = await msg.chat.ask("ꜱᴇɴᴅ ᴛʜᴇ ᴀᴍᴏᴜɴᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ...", filters=filters.text)
         if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**ᴀᴍᴏᴜɴᴛ** ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ, sᴛᴀʀᴛ ᴀɢᴀɪɴ.")
            return
       await msg.reply(f"hm")
        
        
