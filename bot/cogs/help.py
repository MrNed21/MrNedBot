import discord
from discord.ext import commands


prefix = 'ned '
embed_color = 0x00b3ff


class MyHelp(commands.HelpCommand):
   # !help
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help")
        for cog in mapping.items():
            cog_name = getattr(cog, "qualified_name", "No Category")

   # !help <command>
    async def send_command_help(self, command):
        await self.context.send("This is help command")

   # !help <group>
    async def send_group_help(self, group):
        await self.context.send("This is help group")

   # !help <cog>
    async def send_cog_help(self, cog):
        await self.context.send("This is help cog")


class help(commands.Cog):
    def __init__(self, client):
        self.client = client
        # Setting the cog for the help
        help_command = MyHelp()
        help_command.cog = self # Instance of YourCog class
        client.help_command = help_command


#https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96#start1
#dude i legit could not do this without this tutorial bruhh


def setup(client):
    client.add_cog(help(client))
