from discord.ext import commands
from random import choice


class english(commands.Cog, description='Im doing alright in english'):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sentence(self, ctx):
        '''the sussy imposter went to go vent in front of the crewmate on the space station'''
        characters = [ctx.author, 'Bob', 'Joe', 'Mary', 'Jane']
        objects = ['yummy bread', 'their car']
        past_tense_actions = ['went', 'drove', 'sprinted']
        present_tense_actions = ['bash', 'sell', 'kill']
        places = ['New York', 'Old York', 'New Zealand',
                  'Old Zealand', 'New Mexico', 'Old Mexico']
        await ctx.send(f'{choice(characters)} {choice(past_tense_actions)} to {choice(present_tense_actions)} {choice(objects)} in {choice(places)}.')


def setup(client):
    client.add_cog(english(client))
