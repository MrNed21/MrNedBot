import discord
from discord.ext import commands

prefix = 'ned '
embed_color = 0x00b3ff


class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        # the prefix, name, how to use it (arguements)
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)

    # !help
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help",
                              description='List of Commands',
                              color=embed_color)
        for cog, commands in mapping.items():
            command_signatures = [
                self.get_command_signature(c) for c in commands]
            if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")

                if cog_name != 'No Category':
                    embed.add_field(name=cog_name,
                                    value=cog.description,
                                    inline=False)

        embed.set_thumbnail(
            url="http://clipartmag.com/images/scroll-png-25.png")
        embed.set_footer(
            text=f"For specific parameters try {prefix}help [command/catagory]")

        channel = self.get_destination()
        await channel.send(embed=embed)

   # !help <command>
    async def send_command_help(self, command):
        embed = discord.Embed(title="Help",
                              description=f"{command}, detailed.",
                              color=embed_color)
        embed.add_field(name='Usage',
                        value=self.get_command_signature(command),
                        inline=False)

        embed.add_field(name='Desription',
                        value=command.help,
                        inline=False)
        if command.aliases:
            embed.add_field(name='Aliases',
                            value=command.aliases,
                            inline=False)

        embed.set_thumbnail(
            url="http://clipartmag.com/images/scroll-png-25.png")
        embed.set_footer(
            text=f"For specific parameters try {prefix}help [command/catagory]")

        channel = self.get_destination()
        await channel.send(embed=embed)

   # !help <group>
    async def send_group_help(self, group):
        pass

   # !help <cog>
    async def send_cog_help(self, cog):
        embed = discord.Embed(title="Help",
                              description=f"{cog}, detailed.",
                              color=embed_color)

        for command in cog.walk_commands():
            embed.add_field(name=command,
                            value=f'{prefix}{command}',
                            inline=False)

        embed.set_thumbnail(
            url="http://clipartmag.com/images/scroll-png-25.png")
        embed.set_footer(
            text=f"For specific parameters try {prefix}help [command/catagory]")

        channel = self.get_destination()
        await channel.send(embed=embed)


class help(commands.Cog, description='sends the help command'):
    def __init__(self, client):
        self.client = client
        # Setting the cog for the help
        help_command = MyHelp()
        help_command.cog = self  # Instance of YourCog class
        client.help_command = help_command


#https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96#start1
#dude i legit could not do this without this tutorial bruhh


def setup(client):
    client.add_cog(help(client))
