from discord.ext import commands
import json
import random
file = r"/app/bot/data/nfts"
data = open(file, 'r')
nfts = []
for x in data:
    nfts.append(x)


class crypto(commands.Cog, description='fucking monkey nfts'):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nft(self, ctx):
        '''funni monkie'''

        await ctx.send(random.choice(nfts))


def setup(client):
    client.add_cog(crypto(client))
