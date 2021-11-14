from discord import *
from discord.ext import commands
import random

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

    @commands.Cog.listener()
    async def on_message(self, ctx):
        await ctx.reply("i'm dad") if ctx.message.author.id != self.bot.user.id else None

def setup(bot):
    bot.add_cog(Main(bot))