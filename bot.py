# bot.py
import os
import random

from discord import *
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='c!')
client = Client()

@bot.command(name='senkobread')
async def senko(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/795829520162357298.png?v=1")

@bot.command(name='embedtest')
async def embedtest(ctx):

    colorcode = int("0x%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 16)

    testembed = Embed(title="Test Title",description="Test Description",color=colorcode)
    
    await ctx.send(embed=testembed)

bot.run(TOKEN)
