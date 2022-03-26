import discord
from discord.ext import commands
import time


class ping(commands.Cog):
    """Sends the help message"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        '''Check the latency of the bot'''
        start = time.perf_counter()
        await ctx.trigger_typing()
        end = time.perf_counter()
        ping = round((end-start)*1000)
        embed = discord.Embed(title="Ping:", description=ping)
        embed.set_thumbnail(
            url="http://cliparts.co/cliparts/8c6/ozR/8c6ozRoxi.png")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ping(client))
