import logging
import sys
import time
import pyromod.listen
from pyrogram import Client, errors
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

LOGGER = logging.getLogger("pyrogram").setLevel(logging.WARNING)




#Config
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")


#Client
acebot = Client("aceBot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

#info
botin = acebot.get_me()
BOT_ID = botin.id
BOT_NAME = botin.first_name + (botin.last_name or "")
BOT_USERNAME = botin.username
BOT_MENTION = botin.mention
BOT_DC_ID = botin.dc_id
