# bot.py
import os
import random

from dotenv import load_dotenv
from discord import *
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

gameStatus = "raid shadow legends"

activity = Game(name=gameStatus)
# activity = Streaming(name="!help", url="twitch_url_here")
# activity = Activity(type=ActivityType.listening, name="!help")
# activity = Activity(type=ActivityType.watching, name="!help")

bot = commands.Bot(command_prefix='c!', activity=activity, status=Status.idle)
client = Client(intents=Intents.all())
slash = SlashCommand(client, sync_commands=True)

# 738488607261851748 Awesome Realm Official
# 674791516249653277 CAS Testing Server
testServers = [738488607261851748, 674791516249653277]

@bot.command(name='senkobread')
async def senko(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/795829520162357298.png?v=1")

@bot.command(name='embedtest')
async def embedtest(ctx):
    colorcode = int("0x%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 16)
    testembed = Embed(title="Test Title",description="Test Description",color=colorcode)
    await ctx.send(embed=testembed)

bot.run(TOKEN)
