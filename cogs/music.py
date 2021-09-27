import discord
from discord.ext import commands
import os
import youtube_dl
import ffmpeg

class MusicCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["masuk"])
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.reply("Kamu tidak berada di voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await voice_channel.move_to(voice_channel)



    @commands.command(aliases=["dc"])
    async def disconnect(self, ctx):
        if ctx.voice_client is None:
            await ctx.reply("Bot tidak berada dalam voice channel!")
        else:
            await ctx.voice_client.disconnect()

    @commands.command(aliases=["p"])
    async def play(self, ctx, url = None):
        if url is None:
            await ctx.reply("Masukan url youtube!")



def setup(bot):
    bot.add_cog(MusicCommand(bot))