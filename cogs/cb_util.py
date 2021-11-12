# Make sure to update all values in bot.py
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

prefix = 'c!'

testServers = [895356775941939262] # BOT-TESTING

bot_owners  = [786448912587948052]
bot_masters = [786448912587948052]

channel_ids = {'BT-casbot'          : 895359225553907792,
               'CC3-general'        : 814158379207491616,
               'CC3-bot-commands'   : 814158830392311838}

free_storage = {'CHANNEL' : 896612054423703583,
                'msg_main' : None}

testvar = "cheezburger"

cog_exts = ['core', 'admin', 'test']