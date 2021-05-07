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
client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

testServers = [738488607261851748]

@slash.slash(name="ping")
async def _ping(ctx):
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

@slash.slash(name="hello", guild_ids=testServers)
async def hello(ctx):
    await ctx.send("Hello Joe!")

@bot.command(name='senkobread')
async def senko(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/795829520162357298.png?v=1")

@bot.command(name='embedtest')
async def embedtest(ctx):

    colorcode = int("0x%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 16)

    testembed = Embed(title="Test Title",description="Test Description",color=colorcode)

    await ctx.send(embed=testembed)

bot.run(TOKEN)
