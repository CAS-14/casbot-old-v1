from discord import *
from discord.ext import commands
import cogs.cb_util as util
from firebase_admin import db

def register(userid):
        ref = db.reference("/currency/")
        if userid in ref.get():
            return "User already registered"
        ref.update({userid: {"balance":1000}})

def bset(userid, bal):
    db.reference(f"/currency/{userid}").update({"balance":bal})

def bget(userid):
    return db.reference(f"/currency/{userid}/balance/").get()

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bal(self, ctx):
        register(ctx.author.id)
        await ctx.send(":moneybag: Your balance is $"+str(bget(ctx.author.id)))

    @commands.command()
    async def gain(self, ctx, amount):
        register(ctx.author.id)
        if not util.checkMaster(ctx.author.id):
            await ctx.send(":x: Access denied. You must be a **Bot Master** to use this command.")
            return
        
        bset(ctx.author.id, bget(ctx.author.id)+int(amount))
        await ctx.send(f":money_with_wings: Added ${amount} to your balance. You now have ${bget(ctx.author.id)}")

def setup(bot):
    bot.add_cog(Test(bot))