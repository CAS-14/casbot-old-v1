# bot.py
import os
from discord import *
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')
# TOKEN = "MANUAL OVERRIDE"

# activity = Game(name=gameStatus)
# activity = Streaming(name="c!help", url="twitch_url_here")
# activity = Activity(type=ActivityType.listening, name="!help")
# activity = Activity(type=ActivityType.watching, name="!help")

bot = commands.Bot(command_prefix='c!', status=Status.idle)
# client = Client(intents=Intents.all())

"""
extensions = ['admin', 'core', 'test']
for ext in extensions:
    bot.load_extension('cogs.cog_'+ext)
"""

bot.load_extension('cogs.cog_core')
bot.load_extension('cogs.cog_admin')
bot.load_extension('cogs.cog_test')

@bot.event
async def on_ready():
    channel = bot.get_channel(895359225553907792) # BOT-TESTING channel casbot
    await channel.send(':cold_face: CASbot is online!')

bot.run(TOKEN)
