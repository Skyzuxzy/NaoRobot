import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from NaoRobot.events import register as MEMEK
from NaoRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/dfcf67e42704f844cc49d.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  NAO = f"**Holla {tai}, I'm Skyzu Robot!** \n\n"
  NAO += "🔴 **I'm Working Properly** \n\n"
  NAO += "🔴 **My Master : [xxzu](https://t.me/skyzuex)** \n\n"
  NAO += f"🔴 **Telethon Version : {tlhver}** \n\n"
  NAO += f"🔴 **Pyrogram Version : {pyrover}** \n\n"
  NAO += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/skyzuXrobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/skyzusupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=NAO,  buttons=BUTTON)
