from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
bot = Client(
    "my project",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = BOT_TOKEN
)
START_BUTTONS = [
            [
        InlineKeyboardButton('Appeal', callback_data="HELP")
            ]
        ]
START_MESSAGE = """**This bot is made for support related queries regarding ~ @MultieBot press bellow button for submit appeal.\n\nRequest to all boys and girls don't spoil your future for carding or nonsense/illegal stuff. Don't play with anyone's money earn your own and then spend. Thanks ! Jai hind Jai bharat 🇮🇳
**"""
@bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    await message.reply_text(
                text = START_MESSAGE,
                reply_markup = InlineKeyboardMarkup(START_BUTTONS)
            )
@bot.on_callback_query()
async def callback_query(bot, CallbackQuery):
     if CallbackQuery.data == "HELP":
        PAGE_TEXT = """**Now provide your appeal text with explaination and regarding topics, if payment related appeal then provide your payment reference number if applicable else our team will contact you further**"""
        PAGE_BUTTONS = [
            [
        InlineKeyboardButton('⟲ ʙᴀᴄᴋ', callback_data="DATA2")
            ]
        ]
        await CallbackQuery.edit_message_text(
            PAGE_TEXT,
            reply_markup = InlineKeyboardMarkup(PAGE_BUTTONS)
        )
     if CallbackQuery.data == "DATA2":
       await CallbackQuery.edit_message_text(
            START_MESSAGE,
            reply_markup = InlineKeyboardMarkup(START_BUTTONS)
        )
bot.run()
