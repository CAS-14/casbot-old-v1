from discord import *
from discord.ext import commands
import os
import cogs.config as config

URL_1 = 'https://canary.discord.com/api/webhooks/896608021432631316/20LF9S9UFd5oV86J-tx6LdSMaP71PsOKzjtn69_AAg9uc4twZIb3It4JjJd1kVXdJzNv'
webhook1 = Webhook.from_url(URL_1, adapter=RequestsWebhookAdapter())

tsys_USER = 786448912587948052      # dynamite14
tsys_GENERAL = 814158379207491616   # CC3 general

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
        channel = self.bot.get_channel(tsys_GENERAL) # CC3 general
        await channel.send('**tSys** TO SERVER TEST: Hello World! :hamburger:')

    @commands.Cog.listener()
    async def on_message(self, receive_msg: Message):
        bt_channel = self.bot.get_channel(895359225553907792) # BOT-TESTING channel casbot
        # online_msg = await bt_channel.send('This worked!')

        await self.bot.add_reaction(receive_msg, ':white_check_mark:')

        # forward all messages from CC3 general to DMs
        if receive_msg.channel.id == tsys_GENERAL and not receive_msg.author.bot: # CC3 general
            try:
                target_user = self.bot.get_user(tsys_USER) # dynamite14

                tsys_frd = Embed(title="toriSys", color=receive_msg.author.color, description=receive_msg.content)
                tsys_frd.set_author(name=receive_msg.author.name, icon_url=receive_msg.author.avatar_url)
                tsys_frd.set_footer(text=f"{receive_msg.channel.name} in {receive_msg.guild.name}", icon_url=receive_msg.guild.icon_url)
                target_user.send(embed=tsys_frd)
            except Exception as err:
                receive_msg.channel.send(f":x: **Error:**\n```{err}\n```")

        # forward messages from bot DMs to CC3 generl
        elif receive_msg.author.id == tsys_USER and receive_msg.guild.id is None and not receive_msg.author.bot: # dynamite14 user ID
            try:
                webhook1.send(receive_msg.content)
            except Exception as err:
                receive_msg.channel.send(f":x: **Error:**\n```{err}\n```")

        else:
            pass


def setup(bot):
    bot.add_cog(TSys(bot))