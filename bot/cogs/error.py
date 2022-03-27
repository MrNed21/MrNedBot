
import discord
from discord.ext import commands


class error(commands.Cog):

    def __init__(self, client):
        self.client = client
        '''Send errors in chat'''

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        self.send_error(ctx, error)

    async def send_error(self,ctx,error):
        embed = discord.Embed(title="Oh No! An error occured!",
                              description=error, color=0xff0000)
        embed.set_thumbnail(
            url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fclipground.com%2Fimages%2Fdisassemble-clipart-15.jpg&f=1&nofb=1")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(error(client))
