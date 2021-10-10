# bot.py
import os
from discord import *
from discord.ext import commands
import cogs.config as config

TOKEN = os.getenv('DISCORD_TOKEN')
# TOKEN = "MANUAL OVERRIDE"

# activity = Game(name=gameStatus)
# activity = Streaming(name="c!help", url="twitch_url_here")
# activity = Activity(type=ActivityType.listening, name="!help")
# activity = Activity(type=ActivityType.watching, name="!help")

bot = commands.Bot(command_prefix=config.prefix, status=Status.online)
# client = Client(intents=Intents.all())

"""
extensions = ['admin', 'core', 'test']
for ext in extensions:
    bot.load_extension('cogs.cog_'+ext)
"""

verbose_start = True

@bot.event
async def on_ready():
    bt_channel = bot.get_channel(895359225553907792) # BOT-TESTING channel casbot
    await bt_channel.send(':cold_face: CASbot is online!')
    
    exts = ['core', 'admin', 'test', 'tsys']
    for ext in exts:
        try:
            bot.load_extension('cogs.cog_'+ext)
            await bt_channel.send(':white_checkmark: Cog extension `{ext}` loaded successfully!') if verbose_start else None
        except Exception as err:
            await bt_channel.send(':warning: Could not load cog extension`{ext}`. Error:\n{err}')

bot.run(TOKEN)
