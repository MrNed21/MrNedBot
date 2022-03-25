import discord
from discord.ext import commands


class science(commands.Cog):
    """Sends the help message"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dna(self, ctx, o_seq):
        '''this is a certified failing bio moment'''
        o_seq = o_seq.upper()
        o_seq = o_seq.replace(' ', '')

        p_seq = ''
        np_seq = ''
        for x in range(len(o_seq)):
          if x % 3 == 0:
            p_seq += ' '
          if o_seq[x] == 'A':
            p_seq += 'T'
            np_seq += 'T'
          if o_seq[x] == 'T':
            p_seq += 'A'
            np_seq += 'A'
          if o_seq[x] == 'C':
            p_seq += 'G'
            np_seq += 'G'
          if o_seq[x] == 'G':
            p_seq += 'C'
            np_seq += 'C'

        p_seq = p_seq[1:]

        r_seq = ''
        for x in range(len(np_seq)):
          if x % 3 == 0:
            r_seq += ' '
          if np_seq[x] == 'T':
            r_seq += 'U'
          else:
            r_seq += np_seq[x]

        r_seq = r_seq[1:]

        amino_acid = {
            'PHE': ('UUU', 'UUC'),
            'LEU': ('UUA', 'UUG',
                    'CUU', 'CUC', 'CUA', 'CUG'),
            'SER': ('UCU', 'UCC', 'UCA', 'UCG',
                    'AGU', 'AGC'),
            'TYR': ('UAU', 'UAC'),
            'CYS': ('UGU', 'UGC'),
            'PRO': ('CCU', 'CCC', 'CCA', 'CCG'),
            'HIS': ('CAU', 'CAC'),
            'GLN': ('CAA', 'CAG'),
            'ARG': ('CGU', 'CGC', 'CGA', 'CGG',
                    'AGA', 'ARG'),
            'LLE': ('AUU', 'AUC', 'AUA'),
            'MET': ('AUG'),
            'THR': ('ACU', 'ACC', 'ACA', 'ACG'),
            'ASN': ('AAU', 'AAC'),
            'LYS': ('AAA', 'AAG'),
            'VAL': ('GUU', 'GUC', 'GUA', 'GUG'),
            'ALA': ('GCU', 'GCC', 'GCA', 'GCG'),
            'ASP': ('GUA', 'GAC'),
            'GLU': ('GAA', 'GAG'),
            'GLY': ('GGU', 'GGC', 'GGA', 'GGG'),
            'STOP': ('UAA', 'UAG',
                     'UGA')}

        a_seq = ''
        r_seq = r_seq.split(' ')

        combinations = list(amino_acid.values())
        amino_acid_names = list(amino_acid.keys())

        for x in r_seq:
          for y in combinations:
            if x in y:
              position = combinations.index(y)
              a_seq += amino_acid_names[position]+' '

        a_seq = a_seq[:len(a_seq)-1]

        n_seq = ''
        for x in range(len(o_seq)):
            if x % 3 == 0:
                n_seq += ' '
            n_seq += o_seq[x]

        n_seq = n_seq[1:]

        r_seq = " ".join(r_seq)

        embed = discord.Embed(
            title='DNA Translator:',
            description='help im failing biology',
            color=0x00ff40)
        embed.add_field(name='Original', value=n_seq)
        embed.add_field(name='Base Pair', value=p_seq)
        embed.add_field(name='mRNA Translation', value=r_seq)
        embed.add_field(name='Amino Acid Sequence', value=a_seq)
        embed.set_thumbnail(
            url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.clker.com%2Fcliparts%2F8%2Fd%2Fr%2Fe%2FY%2F0%2Fdna-hi.png&f=1&nofb=1'
        )

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(science(client))
