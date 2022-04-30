from discord.ext import commands
import discord
import json
import random
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf
import os
from datetime import date


def save(ticker):
    today = (date.today())
    y = today.year
    m = today.month
    d = today.day
    if d < 10:
        d = '0'+str(d)

    start = f'{str(y-1)}-{str(m)}-{str(d)}'
    end = f'{str(y)}-{str(m)}-{str(d)}'  # get 1 year ago

    stock = yf.download(ticker, start, end)

    stock['Open'].plot(label=ticker, figsize=(15, 7))

    plt.title(f'1 Year Stock Prices of {ticker}')

    plt.savefig(f'{ticker}.png')

    plt.cla()


class stocks(commands.Cog, description='bears and bulls and the wall street'):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def graph(self, ctx, ticker):
        '''show a graph of a stock'''
        ticker = ticker.upper()
        save(ticker)
        company = yf.Ticker(ticker)
        today = str(date.today())
        last_year = (today[:2]+str(int(today[2:4])-1)+today[4:])

        file = discord.File(fp=f"{ticker}.png", filename=f"{ticker}.png")
        try:
            name = company.info['longName']
        except:
            name = ticker
        embed = discord.Embed(
            title=name, description=f"from: {last_year}\nto: {today}", color=0x00ff11)
        embed.set_image(url=f'attachment://{ticker}.png')
        await ctx.send(file=file, embed=embed)
        os.remove(f'{ticker}.png')

    @commands.command()
    async def fgraph(self, ctx, ticker):
        '''doesnt get the name of the ticker, making faster response'''
        ticker = ticker.upper()
        save(ticker)
        company = yf.Ticker(ticker)
        today = str(date.today())
        last_year = (today[:2]+str(int(today[2:4])-1)+today[4:])

        file = discord.File(fp=f"{ticker}.png", filename=f"{ticker}.png")
        embed = discord.Embed(
            title=ticker, description=f"from: {last_year}\nto: {today}", color=0x00ff11)
        embed.set_image(url=f'attachment://{ticker}.png')
        await ctx.send(file=file, embed=embed)
        os.remove(f'{ticker}.png')


def setup(client):
    client.add_cog(stocks(client))
