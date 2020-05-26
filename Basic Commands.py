import discord
from discord.ext import commands
from discord import Member
from discord.ext import commands, tasks

class Basic(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="**-----Help-----**", description="List of Commands", color=000000) 
        embed.set_author(name="MrNedBot")
        embed.add_field(name=":wrench: Setup:", value="ping: check the bots ping. \n load, unload, reload: do the action to the bots cogs. DEV only. \n addme: sends an invite link for the bot.", inline=False)
        embed.add_field(name=":scales: Moderation:", value="announce: announce a message. (wip) \n clear: clear messages. \n kick: boot out a member. \n ban: go full nuclear. \n unban: maybe dont go nuclear. \n mute: mute a member. **muted role must be called** `Muted`. \n unmute: remove the muted role. must be called `Muted`. ", inline=False)
        embed.add_field(name=":abacus: Math:", value="Bing: idk man \n add: add 2 numbers. wow. \n subtract: subtract 2 numbers. \n multiply: multiply 2 numbers. \n divide: divide 2 numbers. \n exponent: raise the first number to the power of the second. ", inline=False)
        embed.add_field(name=":video_game: Fun:", value="consume: we dont judge what wacky shit you eat. \n ultra_consume: a command you cant use. \n stonks: get your bitcoin price for the big **stonk**. \n Meme: WIP DONT USE.", inline=False)
        embed.add_field(name=":game_die: More Fun!", value="8ball: solve your problems with this simple command! \n roll: roll a die. Ex: 1dx. \n hi: greet the bot, get greeted back. \n search: knockoff dankmemer. \n choose: choose between multiple choices. \n cool: judge if a user is cool. \n yelp: yelp review someone or something. \n coiflip: flip a coin. \n catfact: **100** random catfacts for you late discord needs.", inline=False)
        embed.add_field(name=":incoming_envelope: Text:", value="repeat: repeat a message up to 10 times. You need manage messages because I can see all of you abusive shits. \n x3: repeat a message 3 times. Dont make me lock it up too.", inline=False)
        embed.add_field(name=":money_with_wings: Economy: (WIP DO NOT USE)", value="balance: check you balance. \n transfer: pay another person. \n top10: check out the 10 richest players of the server. \n work: make a living.", inline=False)
        embed.add_field(name=":musical_score: Music: (WIP DO NOT USE)", value="join: summon the bot to your channel. \n leave: kick the bot from your channel. \n play: play a song through youtube video URLs. \n volume: set the volume, for free. *cough* rythm *cough*", inline=False)
        embed.set_footer(text="Credit: Designed by MrNed#9857 with discord.py. \n For more help join: discord.com/invite/eU8DjTe") 
        await ctx.send('sent you the help, check your DMs!')
        await ctx.author.send(embed=embed)

    @commands.command(aliases=['invite'])
    async def addme(self, ctx):
        """sends bot invite link"""
        await ctx.send('https://discordapp.com/oauth2/authorize?client_id=660265353234087936&permissions=8&scope=bot')
        
def setup(client):
    client.add_cog(Basic(client))
