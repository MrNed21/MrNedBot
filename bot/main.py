import asyncio
import os

import discord
from discord.ext import commands, tasks

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

intents = discord.Intents.default()
intents.members = True


def mixedCase(*args):
  """
  Gets all the mixed case combinations of a string

  This function is for in-case sensitive prefixes
  """
  total = []
  import itertools
  for string in args:
    a = map(''.join, itertools.product(
      *((c.upper(), c.lower()) for c in string)))
    for x in list(a):
      total.append(x)

  return list(total)


client = commands.Bot(case_insensitive=True, command_prefix=mixedCase('ned '),
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
