import discord
from discord.ext import commands


prefix = 'ned '
embed_color = 0x00b3ff


class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, input='catagories'):
        '''shows this message. duh.'''
        #synonyms for the things
        catagories = ['catagories', 'cogs', 'modules']
        commands = []
        for cog in self.client.cogs:
            for command in cog.get_commands():
                commands += command
        #DISPLAY ALL COGS
        if input in catagories:
            embed = discord.Embed(
                title="Help", description="List of Catagories", color=embed_color)

            for cog in self.client.cogs:
                embed.add_field(
                    name=cog, value=f'`{prefix}help {cog}`', inline=False)

        #DISPLAY ALL COMMANDS
        elif input == 'commands':
            embed = discord.Embed(
                title="Help", description="List of Commands", color=embed_color)

            for cog in self.client.cogs:
                embed.add_field(
                    name=cog, value=', '.join(cog.commands), inline=False)

        #DISPLAY ALL COMMANDS UNDER CATAGORY
        elif input in self.client.cogs:
            cog = self.client.get_cog(input)
            embed = discord.Embed(
                title="Help", description=f"{input}", color=embed_color)

            for command in cog.get_commands():
                embed.add_field(name=command, value=command.help, inline=False)
        #GET DETAILS FROM COMMAND
        elif input in commands:
            embed = discord.Embed(
                title="Help", description=f"{input}", color=embed_color)

            usage = f'{prefix}{input}{input.usage}'
            if input.usage == None:
                usage = f'{prefix}{input}'

            embed.add_filed(name='Usage',
                            value=usage, inline=False)
            embed.add_field(name='Aliases',
                            value=input.aliases, inline=False
                            )

            embed.add_field(name='Description',
                            value=input.help, inline=False)
        #this stuff doesnt change, same image and footer
        embed.set_thumbnail(
            url="http://clipartmag.com/images/scroll-png-25.png")
        embed.set_footer(
                text=f"For specific parameters try {prefix}help [command/catagory]")
        await ctx.send(embed=embed)

#https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96#start1
#dude i legit could not do this without this tutorial bruhh


def setup(client):
    client.add_cog(help(client))
