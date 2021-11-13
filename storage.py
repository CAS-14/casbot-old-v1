'''
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

elif oper == 'TEST':
                if not util.checkMaster(ctx.author.id):
                    await ctx.send(":x: Access denied. You must be a **Bot Master** to use this command.")
                    return

                testkey = "test"+str(randint(1000,9999))

                await ctx.send(f"Testing `key add {testkey} abc123`")
                await self.key(self, ctx, 'add', testkey, 'abc123')
                await ctx.send(f"Testing `key get {testkey}`")
                await self.key(self, ctx, 'get', testkey)
                await ctx.send(f"Testing `key edit {testkey} xyz789`")
                await self.key(self, ctx, 'edit', testkey, 'xyz789')
                await ctx.send(f"Testing `key get {testkey}`")
                await self.key(self, ctx, 'get', testkey)
                await ctx.send(f"Testing `key delete {testkey}`")
                await self.key(self, ctx, 'delete', testkey)
                await ctx.send(f"Testing `key get {testkey}` (not found, should fail)")
                await self.key(self, ctx, 'get', testkey)
                await ctx.send(f"Testing `key add {testkey}` (no value, should fail")
                await self.key(self, ctx, 'add', testkey)
                await ctx.send(f"Testing `key add {testkey} multi word value`")
                await self.key(self, ctx, 'add', testkey, 'multi', 'word', 'value')
                await ctx.send(f"Testing `key get {testkey}`")
                await self.key(self, ctx, 'get', testkey)
                await ctx.send(f"Testing `key add {testkey} mno456` (already exists, should fail)")
                await self.key(self, ctx, 'add', testkey, 'mno456')
                await ctx.send(f"Test complete. Deleting {testkey}...")
                await self.key(self, ctx, 'delete', testkey)
                await ctx.send(":white_check_mark: Test finished.")
'''