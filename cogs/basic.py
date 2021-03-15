from discord.ext import commands


class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def welcome(self, context):
        '''
        Command to welcome yourself lol
        '''
        author_name = str(context.author)[:-5]
        async with context.channel.typing():
            await context.send("welcome " + author_name + " :)")

    @commands.command()
    async def beep(self, context, *args):
        '''
        Command to get a noice message from my bot :)
        '''
        author_name = str(context.author)[:-5]
        async with context.channel.typing():
            await context.send("boop " + author_name + " :D")
    
    @commands.command()
    async def bye(self, context):
        author_name = str(context.author)[:-5]
        async with context.channel.typing():
            await context.send("bubyee " + author_name + " :)")

    @commands.command()
    async def hello(self, context):
        author_name = str(context.author)[:-5]
        async with context.channel.typing():
            await context.send("henlo " + author_name + " :3")

def setup(bot):
    bot.add_cog(basic(bot))
