import discord
from discord.ext import commands
import datetime
import asyncio
import random

time_now = datetime.datetime.now().strftime('%H:%M %p')


class GiveawayCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gstart")
    @commands.has_any_role("Admin", "Owner")
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def _gstart(self, ctx : commands.Context, mins : int, *, prize : str):
        end = datetime.datetime.now() + datetime.timedelta(seconds=mins*60)
        embed = discord.Embed(
            title="Giveaway Dimulai!",
            description=f"Klik 🎉 untuk join giveaway!",
            color=discord.Color.green()
        )
        embed.add_field(name="Hadiah", value=prize, inline=False)
        embed.add_field(name="Selesai pada", value=f"{end} UTC")
        embed.set_footer(text=f"Giveaway selesai {mins} menit dari sekarang!")

        msg = await ctx.send(embed=embed)

        await msg.add_reaction("🎉")
        await asyncio.sleep(mins*60)

        new_msg = await ctx.channel.fetch_message(msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        if len(users) == 0:
            await ctx.send(f"Tidak ada pemenang karena tidak ada yang mengikuti giveaway ini!")
        elif len(users) > 0:
            winner = random.choice(users)

            await ctx.send(f"Congrats! {winner.mention} telah memenangkan {prize}")



def setup(bot):
    bot.add_cog(GiveawayCommand(bot))


