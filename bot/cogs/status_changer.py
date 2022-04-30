import discord
from discord.ext import commands, tasks
import asyncio
version = 2.1


class status_changer(commands.Cog, description='this has no commands go away'):

    def __init__(self, client):
        self.client = client

    @tasks.loop()
    async def change_status(self):
        """This runs the task to loop these things in the status on discord"""
        while True:
            statuses = [f"Running on {len(self.client.guilds)} servers!",
                        f"Just sitting around",
                        f"Running version {str(version)}"]
            for x in statuses:
                await self.client.change_presence(
                    activity=discord.Game(f'ned help | {x}'),
                    status=discord.Status.do_not_disturb)
                await asyncio.sleep(10)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()
        self.change_status.start()


def setup(client):
    client.add_cog(status_changer(client))
