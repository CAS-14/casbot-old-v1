from discord import *
from discord.ext import commands
import cogs.cb_util as util

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def key(self, ctx, *args):
        try:
            oper = args[0]
            key = args[1] if oper != 'clear' else None
            
        except:
            await ctx.send(embed=Embed(title="Error",description=f"Bad arguments\n\nProper command format: `{util.prefix}key <operation> <key> [value]`\nOperation Type: `add`, `edit`, `get`, `delete`", color=0xff0000))
            return
        else:
            try:
                value = ' '.join(args[2:])
            except:
                value = None

        try:

            async with ctx.typing():

                keystore_channel = self.bot.get_channel(908850430547738685)
                keystore_index = await keystore_channel.fetch_message(908850883385757696)

                keystore_ids = keystore_index.content.replace('KEYSTORES:','').split(',')
                keystores = [] # message format
                for kmi in keystore_ids:
                    keystore = await keystore_channel.fetch_message(int(kmi))
                    keystores.append(keystore)

                current_keystore = keystores[-1]

                if key is not None:
                    key = key.replace('$$ks:', '').replace('$$ks;', '')
                    key = (key[:19]) if len(key) > 20 else key
                if value is not None:
                    value = value.replace('$$ks:', '').replace('$$ks;', '')
                    value = (value[:99]) if len(value) > 100 else value

                all_keys = ''
                for ks in keystores:
                    all_keys += ks.content

                if oper == 'add' and value is not None:
                    if key+'$$ks:' not in all_keys:
                        if len(current_keystore.clean_content) > 1850:
                            current_keystore = await keystore_channel.send(f"$$ks;{key}$$ks:{value}$$ks;")
                            await keystore_index.edit(content=keystore_index.content+','+str(current_keystore.id))

                        else:
                            await current_keystore.edit(content=current_keystore.content+key+'$$ks:'+value+'$$ks;')

                        await ctx.send(f":white_check_mark: Added Key `{key}` with Value `{value}`.")

                    else:
                        await ctx.send(f":x: Key `{key}` already exists in the key database.")

                elif oper == 'get':
                    try:
                        key_scope = all_keys[all_keys.index('$$ks;'+key+'$$ks:'):]
                        key_scope = key_scope[:key_scope.index('$$ks;')+5]
                        value = key_scope[(key_scope.index('$$ks:')+5):key_scope.index('$$ks;')]
                    except ValueError as ve:
                        await ctx.send(f":x: Key `{key}` not found.")
                    except Exception as e:
                        await ctx.send(f":x: `{e}`")
                    else:
                        await ctx.send(f":arrow_right: Key `{key}` has value `{value}`")

                elif oper == 'edit' and value is not None:
                    try:
                        key_scope = all_keys[all_keys.index(key+'$$ks:'):]
                        key_scope = key_scope[:key_scope.index('$$ks;')+5]
                        old_value = key_scope[(key_scope.index('$$ks:')+5):key_scope.index('$$ks;')]
                    except ValueError as ve:
                        await ctx.send(f":x: Key `{key}` not found.")
                    except Exception as e:
                        await ctx.send(f":x: `{e}`")
                    else:
                        old_key_scope = key_scope
                        new_key_scope = key_scope.replace(old_value, value)
                        ind = 0
                        for ks in keystores:
                            ind += 1
                            try:
                                keystore_new = ks.content.replace(old_key_scope, new_key_scope)
                            except:
                                None
                            else:
                                await ks.edit(content=keystore_new)

                        await ctx.send(f":memo: Key `{key}` has been edited.\nOld Value: `{old_value}`\nNew Value: `{value}`")

                elif oper == 'delete':
                    try:
                        key_scope = all_keys[all_keys.index(key+'$$ks:'):]
                        key_scope = key_scope[:key_scope.index('$$ks;')+5]
                        value = key_scope[(key_scope.index('$$ks:')+5):key_scope.index('$$ks;')]
                    except ValueError as ve:
                        await ctx.send(f":x: Key `{key}` not found.")
                    except Exception as e:
                        await ctx.send(f":x: `{e}`")
                    else:
                        ind = 0
                        for ks in keystores:
                            ind += 1
                            try:
                                keystore_new = ks.content.replace(key_scope, '')
                            except:
                                None
                            else:
                                await ks.edit(content=keystore_new)

                        await ctx.send(f":wastebasket: Key `{key}` with value `{value}` has been deleted from the database.")

                elif oper == 'clear':
                    if not util.checkOwner(ctx.author.id):
                        await ctx.send(":x: Access denied. You must be a **Bot Owner** to use this command.")
                        return

                    for ks in keystores:
                        await ks.delete()
                    current_keystore = await keystore_channel.send(f"$$ks;base$$ks:hello world$$ks;")
                    await keystore_index.edit(content="KEYSTORES:"+str(current_keystore.id))

                    await ctx.send(":boom: Key database has been wiped and reset.")
                
                else:
                    await ctx.send(embed=Embed(title="Error",description=f"Bad arguments\n\nProper command format: `{util.prefix}key <operation> <key> [value]`\nOperation Type: `add`, `edit`, `get`, `delete`", color=0xff0000))

        except Exception as e:
            await ctx.send(embed=Embed(title="CODE Error",description=f"```\n{e}\n```", color=0xff0000))

def setup(bot):
    bot.add_cog(Miscellaneous(bot))