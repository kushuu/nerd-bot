from discord.ext import commands
import os

bot = commands.Bot(command_prefix="--")

# bot.load_extension(f'cogs.nerdy')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != "__init__.py":
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('#####')  # hidden for security purposes.
