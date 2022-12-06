import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5393737203:AAHFEhJM5GUPn2Nkz0JogYADV7oL5Lz2tgY")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7405235"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5c9541eefe8452186e9649e2effc1f3f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001780640224"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1164918935"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://xucswobughtoom:7afa9428a6bbd742d2ef0b185e973469d3092b9621b29e3adab2cb395e1f5b14@ec2-44-198-126-181.compute-1.amazonaws.com:5432/dbf51luchvrc81")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001531527328"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first} I Only Store Files For @CineHub4U ")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1164918935 1970772845").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first} <b>You need to join in my Channel @CineHub4U to use me Kindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
