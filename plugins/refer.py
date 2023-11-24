from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton(" 📲   ᴄʟɪᴄᴋ  ᴍᴇ  ᴛᴏ  ʀᴇꜰᴇʀ   📲 " ,url=f"https://telegram.me/share/url?url=https://t.me/RenameV0_Bot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"ʏᴏᴜ  ᴡɪʟʟ  ɢᴇᴛ   5 GB  ᴇxᴛʀᴀ  ᴀᴛ  ᴇᴠᴇʀʏ  ʀᴇꜰᴇʀ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
