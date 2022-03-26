import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx,  thing='catagories'):
        '''Sends this message'''
        if thing == 'catagories':  # send all catagories
            embed = discord.Embed(
                title="Help", description="list of Catagories")

            for cog in self.client.cogs:
                embed.add_field(
                    name=cog, value=f'`ned help {cog}`', inline=False)

            embed.set_footer(
                text="For specific parameters try ned help [command/catagory]")

        elif thing == 'commands':  # get all the commands and send them
            embed = discord.Embed(
                title='Help', description='list of Commands'
                )

            for c in self.client.commands:
                embed.add_field(name=c.name, value=c.help, inline=False)

        else:
            if thing in self.client.cogs:  # get all commands under name of catagory
                kog = self.client.get_cog(thing)
                commands = kog.get_commands()
                embed = discord.Embed(
                    title='Help', description=thing+' commands'
                )

                for c in commands:
                    embed.add_field(name=c,
                                    value=c.help, inline=False)


            elif thing in self.client.walk_commands():
                embed = discord.Embed(
                    title='Help', description=thing
                )
                embed.add_field(name=thing,value=thing.usage)

        embed.set_thumbnail(
            url="http://clipartmag.com/images/scroll-png-25.png")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
