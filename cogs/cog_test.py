from discord import *
from discord.ext import commands
import cogs.cb_config as config

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send(":white_check_mark: Test suceeded.")

    @commands.command()
    async def configtest(self, ctx):
        await ctx.send("Test variable: "+config.testvar)

def setup(bot):
    bot.add_cog(Test(bot))