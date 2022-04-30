import itertools
import asyncio
import os
import json
import discord
from discord.ext import commands, tasks

from datetime import datetime


now = datetime.now()

current_time = now.strftime("%H:%M:%S")


intents = discord.Intents.default()
intents.members = True

version = 2.1


def mixedCase(*args):
  """
  Gets all the mixed case combinations of a string

  This function is for in-case sensitive prefixes
  """
  total = []

  for string in args:
    a = map(''.join, itertools.product(
      *((c.upper(), c.lower()) for c in string)))
    for x in list(a):
      total.append(x)

  return list(total)


client = commands.Bot(case_insensitive=True, command_prefix=mixedCase('ned '),
                      intents=intents)
client.remove_command('help')


print('''
███╗░░░███╗██████╗░███╗░░██╗███████╗██████╗░██████╗░░█████╗░████████╗
████╗░████║██╔══██╗████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██╔████╔██║██████╔╝██╔██╗██║█████╗░░██║░░██║██████╦╝██║░░██║░░░██║░░░
██║╚██╔╝██║██╔══██╗██║╚████║██╔══╝░░██║░░██║██╔══██╗██║░░██║░░░██║░░░
██║░╚═╝░██║██║░░██║██║░╚███║███████╗██████╔╝██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═════╝░░╚════╝░░░░╚═╝░░░

''')


@client.event
async def on_ready():
    #details
    print('-------------------')
    print('Done!')
    print()
    print('Welcome User:')
    print()
    print('Username: ' + client.user.name)
    print('ID: ' + str(client.user.id))

    print()
    print('-------------------')
    print('Current Time:')
    print()
    print('Started: ' + str(current_time))
    print()
    print('-------------------')

print('Loading Cogs...')

cogs_loaded = []
for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        cogs_loaded.append(filename[:-3])
        client.load_extension(f'cogs.{filename[:-3]}')

print('-------------------')
print(f'{len(cogs_loaded)} cogs loaded')
print()

client.run('TOKEN')
