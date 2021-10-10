from discord import *
from discord.ext import commands

import config

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def changeactivity(self, ctx, *args):
        if ctx.author.id in config.bot_masters:
            args = list(args)
            # await ctx.send(args)
            try:
                status_type = args[0]
                new_status = ' '.join(args[1:])
            except:
                await ctx.send(embed=Embed(title="Error",description=f"Not enough arguments\n\nProper command format: `{config.prefix}botactivity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))
            else:
                if len(args) > 1:
                    if status_type == "playing":
                        await self.bot.change_presence(activity=Game(name=new_status))
                        await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Playing {new_status}\".", color=0x00ff00))
                    elif status_type == "streaming":
                        await self.bot.change_presence(activity=Streaming(name=new_status, url="https://google.com"))
                        await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Streaming {new_status}\".", color=0x00ff00))
                    elif status_type == "listening":
                        await self.bot.change_presence(activity=Activity(type=ActivityType.listening, name=new_status))
                        await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Listening to {new_status}\".", color=0x00ff00))
                    elif status_type == "watching":
                        await self.bot.change_presence(activity=Activity(type=ActivityType.watching, name=new_status))
                        await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Watching {new_status}\".", color=0x00ff00))
                    else:
                        await ctx.send(embed=Embed(title="Error",description=f"Improper arguments\n\nProper command format: `{config.prefix}botactivity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))
                else:
                    await ctx.send(embed=Embed(title="Error",description=f"Not enough arguments\n\nProper command format: `{config.prefix}botactivity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))
                
        else:
            await ctx.send(":x: Access denied. You must be a **Bot Master** to use this command.")

def setup(bot):
    bot.add_cog(Admin(bot))