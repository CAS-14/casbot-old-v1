from discord import *
from discord.ext import commands
import random

from firebase_admin.db import reference

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='senkobread')
    async def senko(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/795829520162357298.png?v=1")

    @commands.command(name='embedtest')
    async def embedtest(self, ctx):
        colorcode = int("0x%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 16)
        testembed = Embed(title="Test Title",description="Test Description",color=colorcode)
        await ctx.send(embed=testembed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"CASbot ping: {round(self.bot.latency * 1000)}ms")

    @commands.Cog.listener('on_message')
    async def annoy(self, message):
        await message.channel.send("i'm dad", reference=message.author) if message.author != self.user else None
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(Main(bot))