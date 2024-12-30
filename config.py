import datetime
from os import environ 

class Config:
    API_ID = environ.get("API_ID", "29426486")
    API_HASH = environ.get("API_HASH", "d71ad4ec048ab41677a1a439b21ff0c9")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7991927022:AAEKdQ9jSM8-FqtpVRWVacTacV__n6cFgTY") 
    BOT_SESSION = environ.get("BOT_SESSION", "Forward-Bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb://mongo:********@autorack.proxy.rlwy.net:52526")
    DATABASE_NAME = environ.get("DATABASE_NAME", "anonymous")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5976437467').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002244796953'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
