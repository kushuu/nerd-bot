from discord.ext import commands
import discord
import praw
import random
import os
from dotenv import load_dotenv

load_dotenv()

REDDIT_SECRET = os.getenv('REDDIT_SECRET')
REDDIT_APP_ID = os.getenv('REDDIT_APP_ID')

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
        Categories available : nerd,physics,geography,shower thoughts,geeky,facts
        '''
        if len(args) == 0:
            async with context.channel.typing():
                await context.send("Add nerd/physics/geography/shower thoughts/geeky/facts as an argument")
            return
        memeType = args[0]
        if self.reddit:
            if memeType == "nerd":
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

            elif memeType == "geography":
                chosen_sub = "GeographyTrivia"
                submissions = self.reddit.subreddit(chosen_sub).hot()
                post = random.randint(1, 10)
                for _ in range(post):
                    submission = next(x for x in submissions if not x.stickied)

                await context.send(submission.url)
                
            elif memeType == "shower" and args[1] == "thoughts":
                chosen_sub = "nerdshowerthoughts"
                submissions = self.reddit.subreddit(chosen_sub).hot()
                post = random.randint(1, 10)
                for _ in range(post):
                    submission = next(x for x in submissions if not x.stickied)

                await context.send(submission.url)
            
            elif memeType == "geeky":
                chosen_sub = "ProgrammerHumor"
                submissions = self.reddit.subreddit(chosen_sub).hot()
                post = random.randint(1, 10)
                for _ in range(post):
                    submission = next(x for x in submissions if not x.stickied)

                await context.send(submission.url)

            elif memeType == "facts":
                chosen_sub = "facts"
                submissions = self.reddit.subreddit(chosen_sub).hot()
                post = random.randint(1, 10)
                for _ in range(post):
                    submission = next(x for x in submissions if not x.stickied)

                await context.send(submission.url)

            else:
                async with context.channel.typing():
                    await context.send("Refer to help section to see all the possible meme categories available here hehe")

            
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