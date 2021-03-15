from discord.ext import commands
import discord
import praw
import random

REDDIT_SECRET = "FXKmTW5GP83AoafbLQIGXcxqsdMRPA"
REDDIT_APP_ID = "yfeq3lCwPqADkw"


class Nerdy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_SECRET:
            self.reddit = praw.Reddit(client_id = REDDIT_APP_ID, client_secret = REDDIT_SECRET, user_agent = "nerdy discord bot hehe")

    @commands.command()
    async def meme(self, context, *args):
        '''
        Command to get physics/general nerdy memes.
        Categories available : nerd/physics
        '''
        if len(args) == 0:
            async with context.channel.typing():
                await context.send("Add nerd/physics as an argument")
            return
        memeType = args[0]
        if memeType == "nerd":
            if self.reddit:
                chosen_sub = "Nerdjokes"
                submissions = self.reddit.subreddit(chosen_sub).hot()
                post = random.randint(1, 10)
                for _ in range(post):
                    submission = next(x for x in submissions if not x.stickied)
                
                await context.send(submission.url)

        elif memeType == "physics":
            chosen_sub = "physicsmemes"
            submissions = self.reddit.subreddit(chosen_sub).hot()
            post = random.randint(1, 10)
            for _ in range(post):
                submission = next(x for x in submissions if not x.stickied)

            await context.send(submission.url)

        else:
            async with context.channel.typing():
                await context.send("Refer to help section to see all the possible meme categories available here hehe")


    @commands.command()
    async def bored(self, context):
        author_name = str(context.author)[:-5]
        async with context.channel.typing():
            await context.send("abhyas kar nalayak " + author_name + " -.-")

            
    @commands.command()
    async def eval(self, context, *args):
        '''
        Evaluate simple mathematical expressions :)
        '''
        if len(args) < 1:
            await context.send("Enter an expression first (:")
            return
        
        ans = str(eval(args[0]))
        await context.send("Your expression evaluates to: " + ans)

def setup(bot):
    bot.add_cog(Nerdy(bot))