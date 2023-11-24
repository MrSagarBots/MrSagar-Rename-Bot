from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """
🦋 <b>𝐅𝐫𝐞𝐞 𝐏𝐥𝐚𝐧 𝐔𝐬𝐞𝐫 🦋</b>
      • <b>Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ </b>: 10GB
      • <b>Pᴀʀᴀʟʟᴇʟ Pʀᴏᴄᴇss </b>: Unlimited
      • <b>Uᴘʟᴏᴀᴅ 4GB Fɪʟᴇs </b>: No
      • <b>Tɪᴍᴇ Gᴀᴘ </b>: 5 Minutes
      • <b>Pʀɪᴄᴇ </b>: ₹0  Pᴇʀ Mᴏɴᴛʜ
 
 🪙 <b>𝐒𝐢𝐥𝐯𝐞𝐫 𝐓𝐢𝐞𝐫 🪙</b> 
      • <b>Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ </b>: 20GB
      • <b>Pᴀʀᴀʟʟᴇʟ Pʀᴏᴄᴇss </b>: Unlimited
      • <b>Uᴘʟᴏᴀᴅ 4GB Fɪʟᴇs </b>: Yes
      • <b>Tɪᴍᴇ Gᴀᴘ </b>: 30 Seconds
      • <b>Pʀɪᴄᴇ </b>: ₹39  Pᴇʀ Mᴏɴᴛʜ
 
 💫 <b>𝐆𝐨𝐥𝐝 𝐓𝐢𝐞𝐫 💫</b>
      • <b>Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ </b>: 50GB
      • <b>Pᴀʀᴀʟʟᴇʟ Pʀᴏᴄᴇss </b>: Unlimited
      • <b>Uᴘʟᴏᴀᴅ 4GB Fɪʟᴇs </b>: Yes
      • <b>Tɪᴍᴇ Gᴀᴘ </b>: 15 Seconds
      •<b> Pʀɪᴄᴇ </b>: ₹89  Pᴇʀ Mᴏɴᴛʜ
 
 💎 <b>𝐃𝐢𝐚𝐦𝐨𝐧𝐝 𝐓𝐢𝐞𝐫 💎</b>
      • <b>Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ </b>: Unlimited
      • <b>Pᴀʀᴀʟʟᴇʟ Pʀᴏᴄᴇss </b>: Unlimited
      • <b>Uᴘʟᴏᴀᴅ 4GB Fɪʟᴇs </b>: Yes
      • <b>Tɪᴍᴇ Gᴀᴘ </b>: 0 Seconds
      • <b>Pʀɪᴄᴇ </b>: ₹149  Pᴇʀ Mᴏɴᴛʜ

"""
	keybord = InlineKeyboardMarkup(
                [
                    [
            InlineKeyboardButton('ᴄᴏɴᴛᴀᴄᴛ  ᴛᴏ  ᴏᴡɴᴇʀ  ❣️',url='https://t.me/MrSagar0')
            ],
                    [
            InlineKeyboardButton('ʙᴜʏ   ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ   😊',url='https://t.me/MrSagar0')
            ],
                    [
                        InlineKeyboardButton("Cancel", callback_data = "cancel")
                    ]
                ]
            )
	await update.message.edit(text = text, disable_web_page_preview=True, reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """
🦋 <b>𝐅𝐫𝐞𝐞 𝐏𝐥𝐚𝐧 𝐔𝐬𝐞𝐫 🦋</b>
      • <b>Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ </b>: 10GB
      • <b>Pᴀʀᴀʟʟᴇʟ Pʀᴏᴄᴇss </b>: Unlimited
      • <b>Uᴘʟᴏᴀᴅ 4GB Fɪʟᴇs </b>: No
      • <b>Tɪᴍᴇ Gᴀᴘ </b>: 5 Minutes
      • <b>Pʀɪᴄᴇ </b>: ₹0  Pᴇʀ Mᴏɴᴛʜ
 
 🪙 <b>𝐒𝐢𝐥𝐯𝐞𝐫 𝐓𝐢𝐞𝐫 🪙</b> 
      • <b>Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ </b>: 20GB
      • <b>Pᴀʀᴀʟʟᴇʟ Pʀᴏᴄᴇss </b>: Unlimited
      • <b>Uᴘʟᴏᴀᴅ 4GB Fɪʟᴇs </b>: Yes
      • <b>Tɪᴍᴇ Gᴀᴘ </b>: 30 Seconds
      • <b>Pʀɪᴄᴇ </b>: ₹39  Pᴇʀ Mᴏɴᴛʜ
 
 💫 <b>𝐆𝐨𝐥𝐝 𝐓𝐢𝐞𝐫 💫</b>
      • <b>Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ </b>: 50GB
      • <b>Pᴀʀᴀʟʟᴇʟ Pʀᴏᴄᴇss </b>: Unlimited
      • <b>Uᴘʟᴏᴀᴅ 4GB Fɪʟᴇs </b>: Yes
      • <b>Tɪᴍᴇ Gᴀᴘ </b>: 15 Seconds
      •<b> Pʀɪᴄᴇ </b>: ₹89  Pᴇʀ Mᴏɴᴛʜ
 
 💎 <b>𝐃𝐢𝐚𝐦𝐨𝐧𝐝 𝐓𝐢𝐞𝐫 💎</b>
      • <b>Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ </b>: Unlimited
      • <b>Pᴀʀᴀʟʟᴇʟ Pʀᴏᴄᴇss </b>: Unlimited
      • <b>Uᴘʟᴏᴀᴅ 4GB Fɪʟᴇs </b>: Yes
      • <b>Tɪᴍᴇ Gᴀᴘ </b>: 0 Seconds
      • <b>Pʀɪᴄᴇ </b>: ₹149  Pᴇʀ Mᴏɴᴛʜ
"""
	keybord = InlineKeyboardMarkup(
                [
                    [
            InlineKeyboardButton('ᴄᴏɴᴛᴀᴄᴛ  ᴛᴏ  ᴏᴡɴᴇʀ  ❣️',url='https://t.me/MrSagar0')
            ],
                    [
            InlineKeyboardButton('ʙᴜʏ   ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ   😊',url='https://t.me/MrSagar0')
            ],
                    [
                        InlineKeyboardButton("Cancel", callback_data = "cancel")
                    ]
                ]
            )
	await message.reply_text(text = text, disable_web_page_preview=True, reply_markup = keybord)
