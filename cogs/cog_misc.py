from discord import *
from discord.ext import commands
import cogs.cb_util as util
from firebase_admin import db
import json

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def key(self, ctx, oper, key=None, *args):

        value = ' '.join(args)
        value = False if value == '' else value

        # key = key[:31] if len(key) > 32 else key if key else None
        # value = value[:1023] if len(value) > 1024 else value if value else None

        # await ctx.send(f"**Debug**\n`oper={oper}`\n`key={key}`\n`value={str(value)}`\n")

        try:
            await ctx.trigger_typing()

            ref = db.reference('/custom-key-values/')
            refk = db.reference(f'/custom-key-values/{key}/')

            if oper == 'add' and value:
                if key not in ref.get():
                    ref.update({key: value})

                    await ctx.send(f":white_check_mark: Added Key `{key}` with Value `{value}`")

                else:
                    await ctx.send(f":x: Key `{key}` already exists in the key database.")

            elif oper == 'get' and key:
                value = refk.get() if key in ref.get() else None
                if value:
                    await ctx.send(f":arrow_right: Key `{key}` has value `{value}`")
                else: 
                    await ctx.send(f":x: Key `{key}` not found.")

            elif oper == 'edit' and value:
                if key in ref.get():
                    old_value = refk.get()
                    refk.set(value)
                    await ctx.send(f":memo: Key `{key}` has been edited.\nOld Value: `{old_value}`\nNew Value: `{value}`")
                
                else:
                    await ctx.send(f":x: Key `{key}` not found.")

            elif oper == 'delete' and key:
                if key in ref.get():
                    value = refk.get()
                    refk.delete()
                    await ctx.send(f":wastebasket: Key `{key}` with value `{value}` has been deleted from the database.")
                
                else:
                    await ctx.send(f":x: Key `{key}` not found.")

            elif oper == 'clear':
                if not util.checkOwner(ctx.author.id):
                    await ctx.send(":x: Access denied. You must be a **Bot Owner** to use this command.")
                    return

                with open("default_db.json", "r") as f:
                    file_contents = json.load(f)
                ref.set({"base":"default"})

                await ctx.send(":boom: Key database has been wiped and reset.")
            
            elif oper == 'list':
                if not util.checkMaster(ctx.author.id):
                    await ctx.send(":x: Access denied. You must be a **Bot Master** to use this command.")
                    return

                await ctx.send(f":scroll: All keys:\n```\n{ref.get()}\n```")
            
            else:
                await ctx.send(embed=Embed(title="Error",description=f"Bad arguments\n\nProper command format: `{util.prefix}key <operation> <key> [value]`\nOperation Type: `add`, `edit`, `get`, `delete`", color=0xff0000))

        except Exception as e:
            await ctx.send(embed=Embed(title="CODE Error",description=f"```\n{e}\n```", color=0xff0000))

def setup(bot):
    bot.add_cog(Miscellaneous(bot))