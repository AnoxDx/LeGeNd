from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
bot = Client(
    "my project",
    api_id = "10534530",
    api_hash = "8760d7849212237231adda6255eec300",
    bot_token = "5656569490:AAGMMWe-4aLXg14ZiKmxgjYSy_t0J05dbS4"

)
START_BUTTONS = [
            [
        InlineKeyboardButton('Appeal', callback_data="HELP")
            ]
        ]

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
