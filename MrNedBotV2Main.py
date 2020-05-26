import discord
from discord.ext import commands
from discord import Member
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import random
import os
from itertools import cycle
import json
import praw
import youtube_dl
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
import time
import sqlite3

#startup and background task:
client = commands.Bot(command_prefix = 'ned ')
status = cycle(['ned help | https://discord.gg/', 'ned help |',f'ned help | on {len(client.guilds)} servers | version 2.5'])
client.remove_command('help')

#prints something when the bot is online
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('ned help | https://discord.gg/uPq6mnd'))
    change_status.start()
    print('MrNedBotV2 is online.')

#check

#error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used. Check ned help for a list of commands.')
    else:
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the permission to use this command.')
        else:
            await ctx.send('Oops! I encountered an error. Check if you are using the command correctly.') 
        
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(next(status)))

#check
def is_it_me(ctx):
    return ctx.author.id == 604989726444879911

#check ping of bot
@client.command()
async def ping(ctx):
    "Check the ping of the bot"
    await ctx.send(f'Pong!: {round(client.latency * 1000)}ms')
        
#Cog load
@client.command()
@commands.check(is_it_me)
async def load(ctx, extension):
    "Load Files"
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
    "Unload Files"
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.check(is_it_me)
async def reload(ctx, extension):
    "Reload Files"
    client.unload_extension(f'catagories.{extension}')
    client.load_extension(f'catagories.{extension}')
    await ctx.send('reloaded cogs')
            
for filename in os.listdir('./catagories'):    
    if filename.endswith('.py'):
        client.load_extension(f'catagories.{filename[:-3]}')
    
#runs_the_bot
client.run('NjYwMjY1MzUzMjM0MDg3OTM2.XpOX1A.mM0tfIDtxHtWeGxShDpT4xM-7PI')
