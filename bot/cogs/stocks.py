import discord
from discord.ext import commands
import yfinance
import plotly.graph_objects as go
import os
import kaleido


class stock(commands.Cog, description='experimenting with stock stuff'):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def graph(self, ctx, symbol):
        symbol = symbol.upper()

        ticker = yfinance.Ticker(symbol)
        hist = ticker.history(period='1y')
        fig = go.Figure(data=go.Scatter(
            x=hist.index,
            y=hist['Close'],
            mode='lines+markers'))

        fig.write_image("graph.png")

        embed = discord.Embed()
        embed.add_field(name=symbol, value="1 year history", inline=False)
        file = discord.File(filename="graph.png")
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)

        os.remove("graph.png")


def setup(client):
    client.add_cog(stock(client))
