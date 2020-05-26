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
import praw
import aiohttp
import io

class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    def spalex(ctx):
        return ctx.author.id == 590649033282945045

    def jay(ctx):
        return ctx.author.id == 702874736480223302

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun online')

    #Fun--------------------------------------------------------------------------- 

    #Math
    @commands.command()
    async def add(self, ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    @commands.command()
    async def subtract(self, ctx, left: int, right: int):
        """Subtracts two numbers together."""
        await ctx.send(left - right)

    @commands.command()
    async def multiply(self, ctx, left: int, right: int):
        """Multiplies two numbers together."""
        await ctx.send(left * right)

    @commands.command()
    async def divide(self, ctx, left: int, right: int):
        """Divides two numbers together."""
        await ctx.send(left / right)

    @commands.command()
    async def exponent(self, ctx, left: int, right: int):
        """raises the first number to the power of the value of the second number """
        await ctx.send(left ** right)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def repeat(self, ctx, times: int, repeat):
        """Repeats a message multiple times."""
        if times <= 10:
            for i in range(times):
                await ctx.send(repeat)
        else:
            await ctx.send('F*ck off spammer.')
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def x3(self, ctx, text):
        """Repeats a message 3 times."""
        for i in range(3):
            await ctx.send(text)
        
    @commands.command()
    async def consume(self, ctx, food):
        """moaunch"""
        await ctx.send(f'{ctx.message.author.mention} consumed the {food}.')

    @commands.command()
    @commands.check(spalex)
    async def ultra_consume(self, ctx, food):
        await ctx.send(f'consumed the {food} to atoms, erasing it with a black hole, gaining its quantum calories and fufilling your apitite.')

    @commands.command()
    async def stonks(self, ctx):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
        embed = discord.Embed(title="***Stonks***", description="Price for bitcoin (Fellow Stonkers, keep in mind that these numbers update every 1 minute)", color=0) 
        embed.add_field(name="The Current Price for bitcoin is listed below:", value="Bitcoin price is: $" + response['bpi']['USD']['rate'], inline=False)
        embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fif-2M3K1tqk%2Fmaxresdefault.jpg&f=1&nofb=1")
        embed.set_author(name="MrNedBot")
        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        embed = discord.Embed(title="***Meme:***", color=0) 
        embed.add_field(name="here is what we are trying to send, but the code is not working.", value='http://tinyurl.com/2g9mqh', inline=False)
        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(Fun(client))
