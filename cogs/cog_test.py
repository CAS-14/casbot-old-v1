from discord import *
from discord.ext import commands
import cogs.cb_util as util

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send(":white_check_mark: Test suceeded.")

    @commands.command()
    async def utiltest(self, ctx):
        await ctx.send("Test variable: "+util.testvar)

def setup(bot):
    bot.add_cog(Test(bot))