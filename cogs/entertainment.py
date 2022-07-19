import asyncio
import discord
import os

from discord.ext import commands
from .helpers import yt_dl


class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nerd_join(self, context):
        '''
        Makes the bot join the VC you've joined
        '''
        if not context.message.author.voice:
            await context.send("You are not connected to a voice channel")
            return

        voice_client = context.message.guild.voice_client
        if voice_client and voice_client.is_connected():
            await context.send("Bot is already connected to a voice channel.")
            return
        channel = context.message.author.voice.channel
        await channel.connect()

    @commands.command()
    async def nerd_leave(self, context):
        '''
        Makes the bot leave the VC you've joined
        '''
        voice_client = context.message.guild.voice_client
        if voice_client and voice_client.is_connected():
            await context.send(f"Leaving channel: **{context.author.voice.channel}**")
            await voice_client.disconnect()
        else:
            await context.send("The bot is not connected to a voice channel.")
        
    @commands.command()
    async def play(self, context, url):
        '''
        Command to play a song from the passed yt url. (Not very good right now)
        '''
        try :
            server = context.message.guild
            voice_channel = server.voice_client

            if voice_channel is None:
                await self.nerd_join(context)

            async with context.typing():
                filename = await yt_dl.YTDLSource.from_url(url)
                # voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
                voice_channel.play(discord.FFmpegPCMAudio(source='music/'+filename))
                await context.send('Now playing: `{}`'.format(filename))

        except Exception as e:
            print(e)
            await context.send(e)
    
    @commands.command()
    async def play_local(self, context, *, query=None):
        """
        Plays a file from the local filesystem. No argument required!
        """
        voice_channel = context.message.guild.voice_client
        if voice_channel is None:
            await self.nerd_join(context)
        
        song_idx_mapper = {}
        idx = 1
        for file_ in os.listdir('music'):
            song_idx_mapper[idx] = file_
            idx += 1
        
        options = "```Select the index number from the list below to play the song!\n\n"
        for key, val in song_idx_mapper.items():
            options += f"{key}:  {val}\n"
        options += "```"

        await context.send(options)

        def check(msg):
            return msg.author == context.author and msg.channel == context.channel # and msg.content in song_idx_mapper.keys()
        
        try:
            response = await self.bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError as e:
            await context.send("> You didn't send any response in the check time for timeout for this bot (which is 30seconds).")
        
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('music/'+song_idx_mapper[int(response.content)]))

        if context.message.guild.voice_client.is_playing():
            await context.send("Already playing audio.\nQueueing is not yet supported by this bot.")
            return

        context.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
        await context.send('Now playing: `{}`'.format(song_idx_mapper[int(response.content)].split('.')[0]))

    @commands.command()
    async def stop(self, context):
        '''
        Stops the current playing song.
        '''
        voice_client = context.message.guild.voice_client
        if voice_client is None:
            await context.send("Bot not connected to any voice channel.")
            return

        if voice_client.is_playing():
            voice_client.stop()
        else:
            await context.send("The bot is not playing anything at the moment.")

    @commands.command()
    async def pause(self, context):
        '''
        Pauses the current playing song.
        '''
        voice_client = context.message.guild.voice_client
        if voice_client is None:
            await context.send("Bot not connected to any voice channel.")
            return

        if voice_client and voice_client.is_playing():
            voice_client.pause()
        else:
            await context.send("The bot is not playing anything at the moment.")
        return
    
    @commands.command()
    async def resume(self, context):
        '''
        Resumes currently playing song.
        '''
        voice_client = context.message.guild.voice_client
        if voice_client is None:
            await context.send("Bot not connected to any voice channel.")
            return

        if voice_client.is_paused():
            voice_client.resume()
        else:
            await context.send("The bot is not playing anything at the moment.")
        return


def setup(bot):
    bot.add_cog(Entertainment(bot))