import discord
from discord.ext import commands
import json

info = json.load(open("json/info.json", "r", encoding="utf-8_sig"))

#管理者か判定用のデコレータ
def admin_only():
    async def predicate(ctx):
        print(ctx.author.id)
        if ctx.author.id == info["discord_admin_id"]:
            return True
        
        await ctx.respond(f"{ctx.author.name} is not admin", ephemeral=True)
        return False
    return commands.check(predicate)

class AdminOnly(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="admin")
    @admin_only()
    async def admin(
        self,
        ctx: discord.ApplicationContext
    ):
        await ctx.respond(f"{ctx.author.name} is admin")
            
def setup(bot):
    bot.add_cog(AdminOnly(bot))