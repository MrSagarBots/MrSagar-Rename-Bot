import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.progress import humanbytes

from helper.database import  insert ,find_one,used_limit,usertype,uploadlimit,addpredata,total_rename,total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import add_date ,check_expi
CHANNEL = os.environ.get('CHANNEL',"")
import datetime
from datetime import date as date_
STRING = os.environ.get("STRING","")
log_channel = int(os.environ.get("LOG_CHANNEL",""))
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]

#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "Good morning."
elif 12 <= currentTime.hour < 12:
	wish = 'Good afternoon.'
else:
	wish = 'Good evening.'

#-------------------------------
	    
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	try:
	    id = message.text.split(' ')[1]
	except:
	    await message.reply_text(text =f"""Hᴇʟʟᴏ {message.from_user.mention}\n\n➻ Tʜɪꜱ Iꜱ Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ.\n\n➻ Uꜱɪɴɢ Tʜɪꜱ Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ Aɴᴅ Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oғ Yᴏᴜʀ Fɪʟᴇꜱ.\n\n➻ Yᴏᴜ Cᴀɴ Aʟꜱᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ Aɴᴅ Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ.\n\n➻ Tʜɪꜱ Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛꜱ Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜꜱᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.\n\nBᴏᴛ Is Mᴀᴅᴇ Bʏ @MrSagarBots""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚚     BOT CHANNEL    ⚚', url='https://t.me/MrSagarBots')],[InlineKeyboardButton('👨‍💻 OWNER', url='https://t.me/MrSagar0'),InlineKeyboardButton('⚡️ PREMIUM PLANS ⚡️', callback_data = "upgrade")]]))
	    return
	if id:
	    if old == True:
	        try:
	            await client.send_message(id,"ʏᴏᴜʀ  ꜰʀɪᴇɴᴅ  ᴀʟʀᴇᴀᴅʏ  ᴜꜱɪɴɢ  ᴍᴇ")
	            await message.reply_text(text =f"""Hᴇʟʟᴏ {message.from_user.mention}\n\n➻ Tʜɪꜱ Iꜱ Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ.\n\n➻ Uꜱɪɴɢ Tʜɪꜱ Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ Aɴᴅ Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oғ Yᴏᴜʀ Fɪʟᴇꜱ.\n\n➻ Yᴏᴜ Cᴀɴ Aʟꜱᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ Aɴᴅ Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ.\n\n➻ Tʜɪꜱ Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛꜱ Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜꜱᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.\n\nBᴏᴛ Is Mᴀᴅᴇ Bʏ @MrSagarBots""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚚      BOT CHANNEL     ⚚', url='https://t.me/MrSagarBots')],[InlineKeyboardButton('👨‍💻 OWNER', url='https://t.me/MrSagar0'),InlineKeyboardButton('⚡️ PREMIUM PLANS ⚡️', callback_data = "upgrade")]]))
	        except:
	             return
	    else:
	         await client.send_message(id,"ʏᴏᴜ  ᴡᴏɴ  100 ᴍʙ  ᴇxᴛʀᴀ  ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ  😊")
	         _user_= find_one(int(id))
	         limit = _user_["uploadlimit"]
	         new_limit = limit + 104857600
	         uploadlimit(int(id),new_limit)
	         await message.reply_text(text =f"""Hᴇʟʟᴏ {message.from_user.mention}\n\n➻ Tʜɪꜱ Iꜱ Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ.\n\n➻ Uꜱɪɴɢ Tʜɪꜱ Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ Aɴᴅ Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oғ Yᴏᴜʀ Fɪʟᴇꜱ.\n\n➻ Yᴏᴜ Cᴀɴ Aʟꜱᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ Aɴᴅ Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ.\n\n➻ Tʜɪꜱ Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛꜱ Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜꜱᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.\n\nBᴏᴛ Is Mᴀᴅᴇ Bʏ @MrSagarBots""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚚      BOT CHANNEL     ⚚', url='https://t.me/MrSagarBots')],[InlineKeyboardButton('👨‍💻 OWNER', url='https://t.me/MrSagar0'),InlineKeyboardButton('⚡️ PREMIUM PLANS ⚡️', callback_data = "upgrade")]]))
	         

@Client.on_message((filters.private &( filters.document | filters.audio | filters.video )) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text(f"""**{message.from_user.mention}**,\nᴅᴜᴇ  ᴛᴏ  ᴏᴠᴇʀʟᴏᴀᴅ,  ᴏɴʟʏ  ᴄʜᴀɴɴᴇʟ  ᴍᴇᴍʙᴇʀꜱ  ᴄᴀɴ  ᴜꜱᴇ  ᴍᴇ.""",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("🔥  𝙹𝙾𝙸𝙽  𝚄𝙿𝙳𝙰𝚃𝙴  𝙲𝙷𝙰𝙽𝙽𝙴𝙻  🔥" ,url=f"https://telegram.me/{update_channel}") ]   ]))                                                                                         
       		return
       try:
           bot_data = find_one(int(botid))
           prrename = bot_data['total_rename']
           prsize = bot_data['total_size']
           user_deta = find_one(user_id)
       except:
           await message.reply_text("Use About cmd first /about")
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
       	user_type = user_deta["usertype"]
       except:
           await message.reply_text("database has been Cleared click on /start")
           return
           
           
       c_time = time.time()
       
       if user_type=="Free":
           LIMIT = 600
       else:
           LIMIT = 50
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"**Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}**",reply_to_message_id = message.id)
       else:
       		# Forward a single message
           		
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 2147483648
       		used_ = find_one(message.from_user.id)
       		used = used_["used_limit"]
       		limit = used_["uploadlimit"]
       		expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
       		if expi != 0:
       			today = date_.today()
       			pattern = '%Y-%m-%d'
       			epcho = int(time.mktime(time.strptime(str(today), pattern)))
       			daily_(message.from_user.id,epcho)
       			used_limit(message.from_user.id,0)			     		
       		remain = limit- used
       		if remain < int(file.file_size):
       		    await message.reply_text(f"ꜱᴏʀʀʏ,\nɪ  ᴄᴀɴ  ɴᴏᴛ  ᴜᴘʟᴏᴀᴅ  ꜰɪʟᴇꜱ  ᴛʜᴀᴛ  ᴀʀᴇ  ʟᴀʀɢᴇʀ  ᴛʜᴀɴ  ʏᴏᴜʀ  ᴘʟᴀɴ.\n\nɪꜰ  ʏᴏᴜ  ᴡᴀɴᴛ  ᴛᴏ  ʀᴇɴᴀᴍᴇ  ᴍᴏʀᴇ  ꜰɪʟᴇꜱ  ᴛʜᴇɴ  ᴜᴘɢʀᴀᴅᴇ  ʏᴏᴜʀ  ᴘʟᴀɴ.",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ  💳",callback_data = "upgrade") ]]))
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f"ʏᴏᴜ  ᴄᴀɴ  ɴᴏᴛ  ᴜᴘʟᴏᴀᴅ  ᴍᴏʀᴇ  ᴛʜᴀɴ  {humanbytes(limit)}\nUᴜꜱᴇᴅ : {humanbytes(used)}",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ  💳",callback_data = "upgrade") ]]))
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- `{filename}`\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝  ʀᴇɴᴀᴍᴇ",callback_data = "rename"),InlineKeyboardButton("✖️  ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]]))
       		            total_rename(int(botid),prrename)
       		            total_size(int(botid),prsize,file.file_size)
       		        else:
       		            uploadlimit(message.from_user.id,10737418240)
       		            usertype(message.from_user.id,"Free")
	
       		            await message.reply_text(f'Your Plane Expired On {buy_date}',quote=True)
       		            return
       		    else:
       		          	await message.reply_text("Can't upload files bigger than 2GB ")
       		          	return
       		else:
       		    if buy_date:
       		        pre_check = check_expi(buy_date)
       		        if pre_check == False:
       		            uploadlimit(message.from_user.id,10737418240)
       		            usertype(message.from_user.id,"Free")
       		        
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    total_rename(int(botid),prrename)
       		    total_size(int(botid),prsize,file.file_size)
       		    await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- `{filename}`\n\n**File Size** :- {filesize}\n\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝  ʀᴇɴᴀᴍᴇ",callback_data = "rename"),
       		InlineKeyboardButton("✖️  ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]]))
       		
