from discord import *
from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send(":white_check_mark: Test suceeded.")

def setup(bot):
    bot.add_cog(TestCog(bot))