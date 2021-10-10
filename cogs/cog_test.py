from discord import *
from discord.ext import commands
import cogs.config as conf

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send(":white_check_mark: Test suceeded.")

    @commands.command()
    async def configtest(self, ctx):
        await ctx.send("Test variable: "+conf.testvar)

def setup(bot):
    bot.add_cog(Test(bot))