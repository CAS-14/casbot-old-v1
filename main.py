# bot.py
import os
from dotenv import load_dotenv
from discord import *
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')
# TOKEN = "MANUAL OVERRIDE"

prefix = 'c!'
gameStatus = ""

# activity = Game(name=gameStatus)
# activity = Streaming(name="c!help", url="twitch_url_here")
# activity = Activity(type=ActivityType.listening, name="!help")
# activity = Activity(type=ActivityType.watching, name="!help")

bot = commands.Bot(command_prefix=prefix, status=Status.idle)
client = Client(intents=Intents.all())
# slash = SlashCommand(client, sync_commands=True)

# 738488607261851748 Awesome Realm Official
# 674791516249653277 CAS Testing Server
testServers = [738488607261851748, 
               674791516249653277]

bot_owners  = [642527833410895882]

bot_masters = [642527833410895882]

with open("botmasters.txt", "r") as f:
    bot_masters = []
    bot_masters_str = f.readlines()

for userid in bot_masters_str:
    bot_masters.append(int(userid))

@bot.command(name='botactivity')
async def changeactivity(ctx, *args):
    if ctx.author.id in bot_masters:
        args = list(args)
        # await ctx.send(args)
        try:
            status_type = args[0]
            new_status = ' '.join(args[1:])
        except:
            await ctx.send(embed=Embed(title="Error",description=f"Not enough arguments\n\nProper command format: `{prefix}botactivity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))
        else:
            if len(args) > 1:
                if status_type == "playing":
                    await bot.change_presence(activity=Game(name=new_status))
                    await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Playing {new_status}\".", color=0x00ff00))
                elif status_type == "streaming":
                    await bot.change_presence(activity=Streaming(name=new_status, url="https://google.com"))
                    await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Streaming {new_status}\".", color=0x00ff00))
                elif status_type == "listening":
                    await bot.change_presence(activity=Activity(type=ActivityType.listening, name=new_status))
                    await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Listening to {new_status}\".", color=0x00ff00))
                elif status_type == "watching":
                    await bot.change_presence(activity=Activity(type=ActivityType.watching, name=new_status))
                    await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Watching {new_status}\".", color=0x00ff00))
                else:
                    await ctx.send(embed=Embed(title="Error",description=f"Improper arguments\n\nProper command format: `{prefix}botactivity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))
            else:
                await ctx.send(embed=Embed(title="Error",description=f"Not enough arguments\n\nProper command format: `{prefix}botactivity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))
            
    else:
        await ctx.send(":x: Access denied. You must be a **Bot Master** to use this command.")

bot.load_extension("cogs.base")
bot.load_extension("cogs.testcog")

@bot.event
async def on_ready():
    channel = bot.get_channel(895359225553907792)
    await channel.send(':cold_face: CASbot is online!')


bot.run(TOKEN)
