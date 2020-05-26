import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

#Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Imma coggy boi')
#Commands
    @commands.command()
    async def Bing(self, ctx):
        await ctx.send('Bong!')

def setup(client):
    client.add_cog(Example(client))
