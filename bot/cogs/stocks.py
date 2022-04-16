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


def save(ticker):

    start = "2021-01-01"
    end = '2022-1-01'
    stock = yf.download(ticker, start, end)

    stock['Open'].plot(label=ticker, figsize=(30, 14))

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
        file = discord.File(fp=f"{ticker}.png", filename=f"{ticker}.png")
        await ctx.send(file=file)


def setup(client):
    client.add_cog(stocks(client))
