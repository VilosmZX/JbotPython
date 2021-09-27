import discord
import json
import os
from discord.ext import commands
import random

os.chdir("D:\\Project\\EconomyBot")


class BalanceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(BalanceCommand(bot))
