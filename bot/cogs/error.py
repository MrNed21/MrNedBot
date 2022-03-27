
import discord
from discord.ext import commands


def embed_error(self, ctx, error):
    embed = discord.Embed(title="Oh No! An error occured!",
                          description=error, color=0xff0000)
    embed.set_thumbnail(
        url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fclipground.com%2Fimages%2Fdisassemble-clipart-15.jpg&f=1&nofb=1")
    return(embed)


class error(commands.Cog):

    def __init__(self, client):
        self.client = client
        '''Send errors in chat'''

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(embed=self.embed_error(ctx, error))


def setup(client):
    client.add_cog(error(client))
