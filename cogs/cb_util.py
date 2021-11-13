# Make sure to update all values in bot.py
import firebase_admin
from firebase_admin import credentials, db
import json

firebase_admin.initialize_app(credentials.Certificate("firebase_adminsdk.json"), {'databaseURL':"https://casbot-database-default-rtdb.firebaseio.com/"})

def reset_database(confirmation):
    if confirmation == "yes":
        ref = db.reference("/")
        with open("default_db.json", "r") as f:
            file_contents = json.load(f)
        ref.set(file_contents)
        return("Database was reset.")
    else:
        return("Database was not reset.")

def checkMaster(userid):
    if userid in bot_masters:
        return True
    else:
        return False

def checkOwner(userid):
    if userid in bot_owners:
        return True
    else:
        return False

'''
async def get_storage_message(bot, name):
    storage_channel = await bot.get_channel(free_storage['CHANNEL'])
    storage_message = await storage_channel.fetch_message(free_storage[name])
    return storage_message
'''

prefix = 'c!'

testServers = [895356775941939262] # BOT-TESTING

bot_owners  = [786448912587948052]
bot_masters = [786448912587948052]

channel_ids = {'BT-casbot'          : 895359225553907792,
               'CC3-general'        : 814158379207491616,
               'CC3-bot-commands'   : 814158830392311838}

# CHANNEL is a channel ID, others are message IDs
free_storage = {'CHANNEL' : 896612054423703583,
                'rel_ver' : 908838529092689981}

testvar = "cheezburger"

cog_exts = ['core', 'admin', 'test', 'misc', 'currency']