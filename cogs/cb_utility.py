import cb_config as config

def checkMaster(userid):
    if userid in config.bot_masters:
        return True
    else:
        return False

def checkOwner(userid):
    if userid in config.bot_owners:
        return True
    else:
        return False