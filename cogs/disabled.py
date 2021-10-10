@commands.command(name='botmaster')
    async def managemasters(ctx, *args):
        if ctx.author.id in bot_owners:
            args = list(args)
            if args[0] == 'list':
                master_list = ""
                for i in bot_masters:
                    master_list = master_list + "\n" + str(i)
                
                await ctx.send(embed=Embed(title="Bot Masters", description=master_list))

            elif args[0] in ['add','remove']:
                try:
                    this_id = str(args[1])
                except (ValueError, TypeError):
                    await ctx.send(embed=Embed(title="Value Error",description=f"User ID must be an integer.", color=0xff0000))
                except KeyError:
                    await ctx.send(embed=Embed(title="Error",description=f"Not enough arguments\n\nProper command format: `{prefix}botmaster <add|remove> <id>`", color=0xff0000))
                else:
                    if args[0] == 'add':
                        bot_masters.append(this_id)
                        with open("botmasters.txt", 'w') as f:
                            f.writelines(bot_masters)
                    elif args[0] == 'remove':
                        try:
                            bot_masters.remove(this_id)
                        except ValueError:
                            await ctx.send(embed=Embed(title="ID Error",description=f"User ID is not already a botmaster!", color=0xff0000))
                        else:
                            with open("botmasters.txt", 'w') as f:
                                f.writelines(bot_masters)
                    else:
                        await ctx.send(embed=Embed(title="Error",description=f"Improper arguments\n\nProper command format: `{prefix}botmaster <list|add|remove> [id]`", color=0xff0000))
            
            else:
                await ctx.send(embed=Embed(title="Error",description=f"Improper arguments\n\nProper command format: `{prefix}botmaster <list|add|remove> [id]`", color=0xff0000))

        else:
            await ctx.send(":x: Access denied. You must be a **Bot Owner** to use this command.")