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
            await context.send(f"welcome **{author_name}** :)")
        return

    @commands.command()
    async def beep(self, context, *args):
        '''
        Command to get a noice message from my bot :)
        '''
        author_name = str(context.author)[:-5]
        async with context.channel.typing():
            await context.send("boop " + author_name + " :D")
        return
    
    @commands.command()
    async def bye(self, context):
        '''
        Bid farewell to thy companion.
        '''
        author_name = str(context.author)[:-5]
        async with context.channel.typing():
            await context.send("bubyee " + author_name + " :)")
        return

    @commands.command()
    async def hello(self, context):
        '''
        Greet my bot with a good message :)
        '''
        author_name = str(context.author)[:-5]
        async with context.channel.typing():
            await context.send(f"henlo **{author_name}** :3")
        return
    
    @commands.command()
    async def bored(self, context):
        '''
        Try meeeee.
        '''
        author_name = str(context.author)[:-5]
        async with context.channel.typing():
            await context.send(f"abhyas kar nalayak **{author_name}** -.-")
        return


def setup(bot):
    bot.add_cog(basic(bot))
