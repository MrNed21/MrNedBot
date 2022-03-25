from discord.ext import commands
import json
import random
file = r"C:\Users\miste\OneDrive\Documents\Python\Discord\MrNedBot\MrNedBot2.0\data\nft.txt"
data = open(file, 'r')
nfts = []
for x in data:
    nfts.append(x)


class crypto(commands.Cog):
    """Sends the help message"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nft(self, ctx):
        '''funni monkie'''

        await ctx.send(random.choice(nfts))


def setup(client):
    client.add_cog(crypto(client))
