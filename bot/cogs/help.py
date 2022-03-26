import discord
from discord.ext import commands


class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self):
        embed = discord.Embed(title="Help", color=0x00b3ff)
        for cog in self.client.cogs:
            embed.add_field(
                name=cog, value=f'`ned help {cog}`', inline=False)

        channel = self.get_destination()
        embed.set_thumbnail(
            url="http://clipartmag.com/images/scroll-png-25.png")
        embed.set_footer(
                text="For specific parameters try ned help [command/catagory]")
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(
            title="Help", description=command, color=0x00b3ff)
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


class help(commands.Cog):
    def __init__(self, client):
        self.client = client

        help_command = MyHelp()
        help_command.cog = self  # Instance of YourCog class
        client.help_command = help_command

#https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96#start1
#dude i legit could not do this without this tutorial bruhh


def setup(client):
    client.add_cog(help(client))
