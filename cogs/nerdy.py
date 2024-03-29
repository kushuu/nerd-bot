from discord.ext import commands
import discord
import praw
import random
import feedparser
import os
from dotenv import load_dotenv
from math import ceil, floor, sin, cos, tan, exp
from .helpers import caps_all

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
    async def where_am_i(self, context):
        '''
        Gives details about the servr the bot is present in.
        '''

        owner = str(context.guild.owner)
        region = str(context.guild.region)
        guild_id = str(context.guild.id)
        memberCount = str(context.guild.member_count)
        icon = str(context.guild.icon_url)
        desc = context.guild.description
        
        embed = discord.Embed(
            title=context.guild.name + " Server Information",
            description=desc,
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=guild_id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await context.send(embed=embed)

        members=[]
        all_members_details = ''
        async for member in context.guild.fetch_members(limit=150) :
            all_members_details += '> Name : {}\t Status : {}\t Joined at {}\n'.format(member.display_name,str(member.status),str(member.joined_at))
        
        await context.send(all_members_details)
        return

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
        Operations available: arithematic operations, trigonometric functions, exponential, ceil and floor.
        Note: Arguments for trignometric functions should be in radians.
        '''
        if len(args) < 1:
            await context.send("Enter an expression first (:")
            return
        
        try:
            ans = str(eval(args[0]))
        except:
            await context.send("Cant evaluate that expression right now :(")
            return
        await context.send(f"Your expression evaluates to: `{ans}`")

    @commands.command()
    async def news(self, context, *args):
        '''
        Gives latest news/articles in the field of : general, tech and physics
        '''
        if len(args) < 1:
            await context.send("Please enter one of the valid arguments.")
            return
        
        if args[0] == "general":
            NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeeds/296589292.cms")

            entries = NewsFeed.entries
            idx = random.randint(0, len(entries)-1)
            entry = entries[idx]
            await context.send(f"> Published on : {str(entry.published)}\n> Title : {str(entry.title)}\n> {entry.link}")
            
        elif args[0] == "tech":
            NewsFeed = feedparser.parse("https://www.theverge.com/rss/index.xml")

            entries = NewsFeed.entries
            idx = random.randint(0, len(entries)-1)
            entry = entries[idx]
            await context.send(f"> Published on : {str(entry.published)}\n> Title : {str(entry.title)}\n> {entry.link}")

        elif args[0] == "physics":
            NewsFeed = feedparser.parse("https://phys.org/rss-feed/physics-news/")

            entries = NewsFeed.entries
            idx = random.randint(0, len(entries)-1)
            entry = entries[idx]
            await context.send(f"> Published on : {str(entry.published)}\n> Title : {str(entry.title)}\n> {entry.link}")
        else:
            await context.send("Please enter one of the valid arguments.")
            return

    @commands.command()
    async def capital(self, context, *args):
        '''
        Enter countries' names as argument.
        Indian states' capitals are so available :)
        Note: If a country's/state's name is made up of multiple words, write it in " ".
        '''
        if len(args) < 1:
            await context.send("Please give the name of a country to get its capital :)")
            return

        country = args[0].lower()
        if country == "india":
            if len(args) > 1:
                state = args[1].lower()
                cap = caps_all.ind_state(state)
                if cap == -1:
                    await context.send("Enter a valid state or get your spellings checked!")
                    return
                await context.send("Capital of " + str(state) + " : "  + cap)
                return

        elif country == "us" or country == "united states" or country == "united states of america" or country == "usa":
            if len(args) > 1:
                state = args[1].lower()
                cap = caps_all.us_caps(state)
                if cap == -1:
                    await context.send("Enter a valid state or get your spellings checked!")
                    return
                await context.send("Capital of " + str(state) + " : "  + cap)
                return
        
        # print(" ".join(args[:]).lower())
        cap = caps_all.world_caps(" ".join(args[:]).lower())
        if cap == -1:
            await context.send("Enter a valid country or get your spellings checked!")
            return
        await context.send("Capital of " + str(args[0]) + " : "  + cap)

    @commands.command()
    async def position(self, context, *args):
        '''
        Simple command to get latitude and longitude of a US state's capital.
        '''
        if len(args) < 1:
            await context.send("Enter a state to get its position")
            return
        
        state = args[0].lower()
        lat = caps_all.us_state_lat(state)
        longi = caps_all.us_state_long(state)
        if lat == -1 or longi == -1:
            await context.send("Please enter a valid US state or get your spellings checked!")
            return
        await context.send(f"> {state.title()}'s captial : {caps_all.us_caps(state)}\n> {caps_all.us_caps(state)}'s latitude : {str(lat)}\n> {caps_all.us_caps(state)}'s longitude : {str(longi)}")
        place = caps_all.reverseGeocode((lat, longi))
        if place != 0:
            await context.send("https://www.google.com/maps/place/" + place)
        else:
            await context.send("Could not find that location automatically, please try searching on your own hehe")

def setup(bot):
    bot.add_cog(Nerdy(bot))