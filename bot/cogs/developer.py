import discord
from discord.ext import commands
import discord.utils
import time


class developer(commands.Cog, description='developer command'):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def whois(self, ctx, target: discord.Member):
        '''literally spyware / api scrapper'''
        embed = discord.Embed(
            title=target,
            color=0x00cc3d
        )
        embed.set_image(url=target.avatar_url)
        embed.add_field(name='Name ', value=target.name)
        embed.add_field(name='Discriminator', value=target.discriminator)
        embed.add_field(name='ID', value=target.id)
        embed.add_field(name='Highest Role', value=target.top_role)
        embed.add_field(name='Server Permisions',
                        value=target.guild_permissions)
        embed.add_field(name='Created at', value=target.created_at)
        embed.add_field(name='Avatar Hash', value=target.avatar)
        embed.add_field(name='Is Bot?', value=target.bot)
        embed.add_field(name='Activity', value=target.activity)
        embed.add_field(name='Activities', value=target.activities)
        embed.add_field(name='Color', value=target.color)
        embed.add_field(name='Raw Status', value=target.raw_status)
        embed.add_field(name='Desktop Status', value=target.desktop_status)
        embed.add_field(name='Mobile Status', value=target.mobile_status)
        embed.add_field(name='Web Status', value=target.web_status)
        embed.add_field(name='Display Name', value=target.display_name)
        embed.add_field(name='Server', value=target.guild)
        embed.add_field(name='Relationship', value=target.relationship)
        embed.add_field(name='Nickname', value=target.nick)
        embed.add_field(name='Nitro Since', value=target.premium_since)
        embed.add_field(name='Public Flags', value=target.public_flags)
        embed.add_field(name='Roles', value=target.roles)
        embed.add_field(name='System', value=target.system)
        embed.add_field(name='Voice', value=target.voice)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        '''Check the latency of the bot'''
        start = time.perf_counter()
        await ctx.trigger_typing()
        end = time.perf_counter()
        ping = round((end-start)*1000)
        embed = discord.Embed(title="Ping:", description=ping)
        embed.set_thumbnail(
            url="http://cliparts.co/cliparts/8c6/ozR/8c6ozRoxi.png")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(developer(client))
