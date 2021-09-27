import discord
from discord.ext import commands
import asyncio

class RoleCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="addrole")
    @commands.has_any_role("Owner", "Admin", "Moderator")
    async def _addrole(self, ctx : commands.Context, member : discord.Member, role : discord.Role, *, reason : str = None):
        if role in member.roles:
            await ctx.send(f"{member.mention} sudah memiliki role {role.mention}")
        else:
            await member.add_roles(role, reason = reason)
            await ctx.send(f"Role {role.mention} telah ditambahkan kepada {member.mention}")



def setup(bot):
    bot.add_cog(RoleCommand(bot))