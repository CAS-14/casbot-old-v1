import os
from discord import *
from discord.ext import commands
import cogs.config as config

TOKEN = os.getenv('DISCORD_TOKEN')

# activity = Game(name=gameStatus)
# activity = Streaming(name="c!help", url="twitch_url_here")
# activity = Activity(type=ActivityType.listening, name="!help")
# activity = Activity(type=ActivityType.watching, name="!help")

bot = commands.Bot(command_prefix=config.prefix, status=Status.online)

verbose_start = False

@bot.event
async def on_ready():
    bt_channel = bot.get_channel(895359225553907792) # BOT-TESTING channel casbot
    online_msg = await bt_channel.send(':cold_face: CASbot is online!\n')
    
    exts = ['core', 'admin', 'test', 'tsys']
    for ext in exts:
        try:
            bot.load_extension('cogs.cog_'+ext)
            await online_msg.edit(content = online_msg.content + f'\n:white_check_mark: Cog extension `{ext}` loaded successfully!') if verbose_start else None
        except Exception as err:
            await online_msg.edit(content = online_msg.content + f'\n:warning: Could not load cog extension `{ext}`.\n```\n{err}\n```')

bot.run(TOKEN)
