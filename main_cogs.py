import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="--", intents=intents)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != "__init__.py":
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)