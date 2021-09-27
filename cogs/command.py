import discord
from discord.ext import commands
from datetime import datetime
from PIL import Image
from io import BytesIO
import os
import time



time_now = datetime.now().strftime('%H:%M %p')

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo")
    async def _userinfo(self, ctx : commands.Context, member : discord.Member = None):
        if member is None:
            member = ctx.author

        embed = discord.Embed(
            title=f"{member.name}\'s info",
            color=member.color
        )
        is_on_mobile = True if member.is_on_mobile() == True else False
        is_on_mobile = "Yes" if is_on_mobile == True else "No"
        current_activity = member.activity
        current_activity = "No Activity" if current_activity is None else current_activity

        embed.add_field(name="Nickname: ", value=member.mention, inline=False)
        embed.add_field(name="Role: ", value=member.top_role.mention, inline=False)
        embed.add_field(name="Discriminator: ", value=member.name + "#" + member.discriminator, inline=False)
        embed.add_field(name="Created at: ", value=member.created_at.strftime('%m/%d/%Y'), inline=False)
        embed.add_field(name="Joined at: ", value=member.joined_at.strftime('%m/%d/%Y'))
        embed.add_field(name="Using phone: ", value=is_on_mobile, inline=False)
        embed.add_field(name="Current activity: ", value=current_activity, inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requeste by {ctx.author} at {time_now}")

        await ctx.send(embed=embed)

    @commands.command(name="ping")
    async def _ping(self, ctx : commands.Context):
        await ctx.send(f"{round(self.bot.latency), 1} ms 📶")

    @commands.command(name="wanted")
    async def _wanted(self, ctx : commands.Context, member : discord.Member = None):
        if member is None:
            member = ctx.author

        wanted_img = Image.open("D:/Project/EconomyBot/cogs/img/wanted.jpg")
        asset = member.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((344, 274))
        wanted_img.paste(pfp, (59, 236))
        wanted_img.save("D:/Project/EconomyBot/cogs/img/profile.jpg")

        await ctx.send(file = discord.File("D:/Project/EconomyBot/cogs/img/profile.jpg"))
        print("wanted Image sended")
        time.sleep(3)

        os.remove("D:\\Project\\EconomyBot\\cogs\\img\\profile.jpg")
        print("Image deleted")

    @commands.command(name="thumbup")
    async def _thumbupto(self, ctx : commands.Context, member : discord.Member = None):
        if member is None:
            member = ctx.author

        thumbup_img = Image.open("D:/Project/EconomyBot/cogs/img/ok.jpg")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((57, 64))
        thumbup_img.paste(pfp, (83, 71))
        thumbup_img.save("D:/Project/EconomyBot/cogs/img/thumb_profile.jpg")

        await ctx.send(file = discord.File("D:/Project/EconomyBot/cogs/img/thumb_profile.jpg"))
        print("Thumb up image sended")

        time.sleep(3)

        os.remove("D:/Project/EconomyBot/cogs/img/thumb_profile.jpg")
        print("Image deleted")








def setup(bot):
    bot.add_cog(Command(bot))