from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="--")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != "__init__.py":
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)