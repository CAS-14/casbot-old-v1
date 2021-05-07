# bot.py
import os
import random

from dotenv import load_dotenv
from discord import *
from discord.ext import commands
from discord_slash import SlashCommand

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='c!')
client = Client(intents=Intents.all())
slash = SlashCommand(bot, sync_commands=True)

# 738488607261851748 Awesome Realm Official
# 674791516249653277 CAS Testing Server
# 814158378653712455 Chez Cult Remastered
# 765588555010670654 aki's emporium
# 834191823114731563 test
testServers = [738488607261851748, 674791516249653277, 814158378653712455, 765588555010670654, 834191823114731563]

@slash.slash(name="ping")
async def _ping(ctx):
    await ctx.send(f"Pong! ({bot.latency*1000}ms)")

@slash.slash(name="hello", guild_ids=testServers)
async def hello(ctx):
    await ctx.send("Hello Joe!")

@slash.slash(name="anothertest", guild_ids=testServers)
async def anothertest(ctx):
    await ctx.send("efjwefiuwhe")

@bot.command(name='senkobread')
async def senko(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/795829520162357298.png?v=1")

@bot.command(name='embedtest')
async def embedtest(ctx):

    colorcode = int("0x%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 16)

    testembed = Embed(title="Test Title",description="Test Description",color=colorcode)

    await ctx.send(embed=testembed)

bot.run(TOKEN)
