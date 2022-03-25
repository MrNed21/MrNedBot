import discord
from discord.ext import commands

from random import randint, choice


class RNG(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        "Magic 8ball style command"
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Perhaps",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Indubitably",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful.",
                     "YO! you got the 1/23 chance response!"]
        embed = discord.Embed(
            title="**:8ball: The Magic 8Ball: **",
            description="8ball",
            color=0x000000)
        embed.add_field(name="Question:",
                        value=f"{question}", inline=False)
        embed.add_field(
            name="Answer:", value=f"{choice(responses)}", inline=False)
        await ctx.send(embed=embed)

    #dice roll
    @ commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""

        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return
        embed = discord.Embed(
            title='Dice roll',
            description=f'Rolling {rolls} {limit} sided dice.',
            color=0xffffff
        )
        embed.set_thumbnail(
            url='https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fih0.redbubble.net%2Fimage.118255989.1065%2Fsticker%2C375x360.u5.png&f=1&nofb=1')
        result = ', '.join(str(randint(1, limit)) for r in range(rolls))
        embed.add_field(name='Result:', value=result)
        await ctx.send(embed=embed)

    @commands.command(description='best used by pinging 2 people')
    async def choose(self, ctx, *choices: str):
        embed = discord.Embed(
            title='I choose...',
            description=(choice(choices)),
            color=0x4c00ff)
        embed.add_field(name='From', value=choices)
        await ctx.send(embed=embed)

    @commands.command()
    async def yelp(self, ctx, *, review):
        "yelp review"
        stars = ''
        score = randint(1, 5)
        for x in range(score):
            stars = stars+':stars:'
        embed = discord.Embed(
            title=review+':', description=f'Stars: {stars}', color=0xff0000
        )
        embed.set_thumbnail(
            url='https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fsearchengineland.com%2Ffigz%2Fwp-content%2Fseloads%2F2012%2F08%2FScreen-Shot-2012-08-01-at-1.32.34-PM.png&f=1&nofb=1')
        review = [
            'pretty garbage smh',
            'i mean it wasnt that bad',
            'pretty mmmmmmm',
            'kinda gaming',
            '''This past Saturday, January 15, my wife and I went to the Fredericksburg, VA Carrabba's in Central Park for lunch. Our food (sirloin steak and grilled salmon) was delicious and perfectly cooked. Our server, Alyssa, did such an outstanding job that I felt compelled to speak with manager as we left to let him know. We will definitely be going back to this restaurant and highly recommend you do the same!'''
        ]
        embed.add_field(name='MrNedBot said:', value=review[score-1])
        await ctx.send(embed=embed)

    @commands.command()
    async def coinflip(self, ctx):
        '''settle every single dispute ever'''
        chance = randint(1, 12000)
        embed = discord.Embed(
            title='Coinflip:',
            color=0xb1d4dd
        )
        embed.set_thumbnail(
            url='https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fclipartbarn.com%2Fwp-content%2Fuploads%2F2017%2F03%2FGold-coins-coin-clip-art-clipartfox.png&f=1&nofb=1')
        if chance < 3:
            embed.add_field(
                name='Result:', value="LMAO IT LANDED ON ITS SIDE 0.01% LMAO")
        elif chance > 2 and chance < 6004:
            embed.add_field(name='Result:', value="Heads")
        else:
            embed.add_field(name='Result:', value="Tails")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(RNG(client))
