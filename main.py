from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
bot = Client(
    "my project",
    api_id = "10534530",
    api_hash = "8760d7849212237231adda6255eec300",
    bot_token = "5656569490:AAGMMWe-4aLXg14ZiKmxgjYSy_t0J05dbS4"

)
LgenedX = "AnoxDx"
chat_id = -1001679600611
force_channel = "Evonity"
START_PIC = 'https://graph.org/file/77809b5bf1db62f8e6ae5.jpg'
START_MESSAGE = """
**» ᴄʀᴇᴀᴛᴇ ᴠᴏᴛᴇ ᴘᴏʟʟ ꜰᴏʀ ɢɪᴠᴇᴀᴡᴀʏꜱ ᴏʀ ᴏᴛʜᴇʀ ᴘᴜʀᴘᴏꜱᴇꜱ ᴄʜᴇᴄᴋ ᴄᴏᴍᴍᴀɴᴅꜱ ᴜꜱɪɴɢ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ.** \n\n\
**‣ ʟᴇɢᴇɴᴅᴀʀʏ-ᴠᴏᴛᴇ-ʙᴏᴛ**
**‣ Oᴡɴᴇʀ ( @AnoxDx )**\n\n\
**ɪғ ʙᴏᴛ ɴᴏᴛ ᴡᴏʀᴋɪɴɢ ᴛʜᴇɴ ʀᴇᴘᴏʀᴛ ᴛᴏ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ( @EvonixZone ).**"""
START_BUTTONS = [
    [
        InlineKeyboardButton('ᴇᴠᴏɴɪᴛʏ', url='https://t.me/Evonity'),
        InlineKeyboardButton('ꜱᴜᴘᴘᴏʀᴛ', url='https://t.me/EvonixZone')
    ],
    [
        InlineKeyboardButton('✘ ʜᴇʟᴘ ✘', callback_data="HELP")
    ]
]

@bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    await message.reply_photo(
                photo = START_PIC,
                caption = START_MESSAGE,
                reply_markup = InlineKeyboardMarkup(START_BUTTONS)
            )
@bot.on_callback_query()
async def callback_query(bot, CallbackQuery):
     if CallbackQuery.data == "HELP":
        PAGE_TEXT = """✅ 𝗛𝗼𝘄 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗕𝗼𝘁?\n\n\
 **‣ ꜰɪʀꜱᴛ ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴠᴏᴛᴇ-ᴘᴏʟʟ ᴜsɪɴɢ /vote ᴄᴏᴍᴍᴀɴᴅ.**\n\n\
 **‣ ᴛʜᴇɴ ʙᴏᴛ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴘᴀʀᴛɪᴄɪᴘᴀᴛɪᴏɴ ʟɪɴᴋ. ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜɪꜱ ʟɪɴᴋ, ᴜꜱᴇʀꜱ ᴄᴀɴ ᴘᴀʀᴛɪᴄɪᴘᴀᴛᴇ ɪɴ ʏᴏᴜʀ ᴠᴏᴛᴇ-ᴘᴏʟʟ.**\n\n\
 **‣ ʏᴏᴜ ᴄᴀɴ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴠᴏᴛᴇ-ᴘᴏʟʟ ᴜsɪɴɢ /delete ᴄᴏᴍᴍᴀɴᴅ.**
"""
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
VOTEPOLL = """**[⚡] PARTICIPANT DETAILS [⚡]**\n\n
**‣ ᴜꜱᴇʀ: {}**
**‣ ᴜꜱᴇʀ-ɪᴅ: {}**
**‣ ᴜꜱᴇʀɴᴀᴍᴇ: @{}**\n\n
**ɴᴏᴛᴇ: ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ ꜱᴜʙꜱᴄʀɪʙᴇʀꜱ ᴄᴀɴ ᴠᴏᴛᴇ.**\n
**×× ᴄʀᴇᴀᴛᴇᴅ ʙʏ - [ʟᴇɢᴇɴᴅ ʙᴏᴛ](https://t.me/eVoteRobot) ××**
"""
LEGENDBUTTON = (
    [[
        InlineKeyboardButton('⚡0', callback_data="LEGENDOP")
    ]]
)
OHK_BUTTON = (
    [[
        InlineKeyboardButton('post link', url="https://t.me/{chat_id}")
    ]]
)
OP_BRO = """**✅ʏᴏᴜʀ ᴘᴏʟʟ ʜᴀꜱ ʙᴇᴇɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄʀᴇᴀᴛᴇᴅ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘᴏꜱᴛ**"""
@bot.on_message(filters.command('done') & filters.private)
async def done(bot, message):
    await bot.send_photo(chat_id, photo=START_PIC, caption=VOTEPOLL.format(message.from_user.mention, message.from_user.id, message.from_user.username), reply_markup=InlineKeyboardMarkup(LEGENDBUTTON))
    await message.reply(text=OP_BRO, reply_markup=InlineKeyboardMarkup(OHK_BUTTON))
bot.run()
