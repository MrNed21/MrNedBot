import discord
from discord.ext import commands
import plotly.graph_objs as go
import yfinance as yf
import os


class stock(commands.Cog, description='experimenting with stock stuff'):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def graph(self, ctx, symbol):
        symbol = symbol.upper()

        data = yf.download(
            tickers=symbol,
            period='365d',
            interval='15m',
            rounding=bool)

        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='market data'))
        fig.update_layout(title=f' {symbol} share price',
                          yaxis_title='Stock Price (USD)')
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label='15m',
                         step="minute", stepmode="backward"),
                    dict(count=45, label='45m',
                         step="minute", stepmode="backward"),
                    dict(count=1, label='1h', step="hour", stepmode="backward"),
                    dict(count=6, label='6h', step="hour", stepmode="backward"),
                    dict(step="all")
                ])
                )
        )
        fig.write_image("graph.png")

        embed = discord.Embed()
        embed.add_field(name=symbol, value="1 year history", inline=False)
        file = discord.File(
            r"MrNedBot/bot/cogs/graph.png", filename="graph.png")
        embed.set_image(url="attachment://graph.png")
        await ctx.send(file=file, embed=embed)

        #os.remove("graph.png")


def setup(client):
    client.add_cog(stock(client))
