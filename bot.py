import discord 
import os
from discord.ext import commands
from discord.flags import Intents 
from decouple import config 

TOKEN = config('TOKEN')
PREFIX = config('PREFIX')
bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all(), case_insensitive=True)

@bot.event
async def on_ready():
    print(f"{bot.user} is online")

#run cogs 
for filename in os.listdir('./cogs'):
    try:
        if filename.endswith('.py'):
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} has been loaded")
    except Exception as e:
        print("ERROR: " + e)

bot.run(TOKEN)



