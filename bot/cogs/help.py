import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, mapping):
        embed = discord.Embed(title="Help")
        for cog, commands in mapping.items():
           command_signatures = [
               self.get_command_signature(c) for c in commands]
           if command_signatures:
               cog_name = getattr(cog, "qualified_name", "No Category")
               embed.add_field(name=cog_name, value="\n".join(
                    command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
