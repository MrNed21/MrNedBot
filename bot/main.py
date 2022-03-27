import asyncio
import os

import discord
from discord.ext import commands, tasks

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='ned ',
                      intents=intents)
client.remove_command('help')


@tasks.loop()
async def change_status():
    """This runs the task to loop these things in the status on discord"""
    while True:
        statuses = [f"ned help | running on {len(client.guilds)} servers!",
                    "ned help | Just stting around",
                    "ned help | Version 2.0 release!"]
        for x in statuses:
            await client.change_presence(
                activity=discord.Game(x),
                status=discord.Status.do_not_disturb)
            await asyncio.sleep(10)


@client.event
async def on_ready():
    #details
    print('Logged in as:')
    print('Username: ' + client.user.name)
    print('ID: ' + str(client.user.id))

    print()
    #more details
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print('Time:')
    print('Started: ' + str(current_time))
    print()
    print('-------------------')
    await client.change_presence(status=discord.Status.do_not_disturb)

    change_status.start()

print('Cogs Loaded:')
for filename in os.listdir('bot/cogs'):
    if filename.endswith('.py'):
        print(f'{filename[:-3]}')
        client.load_extension(f'cogs.{filename[:-3]}')

print()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
