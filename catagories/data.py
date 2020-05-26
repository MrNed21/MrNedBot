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
from os import system
import time

class data(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Imma coggy boi')
    #Commands
    #@commands.command()
    #def

def setup(client):
    client.add_cog(data(client))
