from discord import *
from discord.ext import commands
import os
import cogs.config as config

URL_1 = os.getenv('TSYS_URL_ONE')
webhook1 = Webhook.from_url(URL_1, adapter=RequestsWebhookAdapter())

# 879364514255077447 dynamite14
# 814158379207491616 CC3 general

class TSys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tsys_status(self, ctx):
        await ctx.send("**tSys** is configured for a TEST with `dynamite14#8880` (DMid `879364514255077447`)")

    @commands.command()
    async def tsys_senddm(self, ctx):
        channel = self.bot.get_channel(879364514255077447) # dynamite14 x casbot DM
        await channel.send('**tSys** TO DM TEST: Hello World! :monkey:')

    @commands.command()
    async def tsys_sendserver(self, ctx):
        channel = self.bot.get_channel(814158379207491616) # CC3 general
        await channel.send('**tSys** TO SERVER TEST: Hello World! :hamburger:')

    # forward DMs from target to webhook
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.channel.id == 879364514255077447: # dynamite14 x casbot DM
            webhook1.send(message.content)

def setup(bot):
    bot.add_cog(TSys(bot))