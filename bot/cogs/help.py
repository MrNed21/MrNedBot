import discord
from discord.ext import commands


class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", color=0x00b3ff)
        for cog, commands in mapping.items():
           filtered = await self.filter_commands(commands, sort=True)
           command_signatures = [
               self.get_command_signature(c) for c in filtered]
           if command_signatures:
               cog_name = getattr(cog, "qualified_name", "No Category")
               embed.add_field(
                   name=cog_name, value=f'ned help {cog_name}', inline=False)

        channel = self.get_destination()
        embed.set_thumbnail(
            url="http://clipartmag.com/images/scroll-png-25.png")
        embed.set_footer(
                text="For specific parameters try ned help [command/catagory]")
        await channel.send(embed=embed)

    async def send_cog_help(self, cog):
        self.client
        embed = discord.Embed(
            title=f"Help: {cog}", color=0x00b3ff)
        for x in cog.commands:
            embed.add_field(name=x, value=f'ned help {x}', inline=False)
        channel = self.get_destination()
        embed.set_thumbnail(
            url="http://clipartmag.com/images/scroll-png-25.png")
        embed.set_footer(
                text="For specific parameters try ned help [command/catagory]")
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(
            title=f"Help: {command}", color=0x00b3ff)
        embed.add_field(
            name='Usage', value=self.get_command_signature(command))
        embed.add_field(name="Description", value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(
                name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        embed.set_thumbnail(
            url="http://clipartmag.com/images/scroll-png-25.png")
        embed.set_footer(
                text="For specific parameters try ned help [command/catagory]")
        await channel.send(embed=embed)


prefix = 'ned '
embed_color = 0x00b3ff


class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, input='catagories'):
        '''shows this message. duh.'''

        #synonyms for the things
        commands = ['commands']
        catagories = ['catagories', 'cogs', 'modules']

        #DISPLAY ALL COGS
        if input in catagories:
            embed = discord.Embed(
                title="Help", description="list of Catagories", color=embed_color)

            for cog in self.client.cogs:
                embed.add_field(
                    name=cog, value=f'`{prefix}help {cog}`', inline=False)

        #DISPLAY ALL COMMANDS UNDER CATAGORY
        elif input in commands:
            embed = discord.Embed(
                title="Help", description="list of Commands", color=embed_color)

            for cog in self.client.cogs:
                embed.add_field(
                    name=cog, value=', '.join(cog.commands), inline=False)

        #GET DETAILS FROM COMMAND
        elif input in self.client.commands:
            embed = discord.Embed(
                title="Help", description=f"Detail of {input}", color=embed_color)

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
        ctx.send(embed=embed)

#https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96#start1
#dude i legit could not do this without this tutorial bruhh


def setup(client):
    client.add_cog(help(client))
