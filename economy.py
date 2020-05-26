import discord
from discord.ext import commands
import os
from discord.utils import get
from os import system
import sqlite3

class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client
    

    #ca$h dollar
    DIR = os.path.dirname(__file__)
    db = sqlite3.connect(os.path.join(DIR, "BankAccounts.db"))
    SQL = db.cursor()
    START_BALANCE = 100.00
    C_NAME = "NedCoins"

    @commands.command(pass_context=True, brief="Shows users balance", aliases=["bal"])
    async def balance(self, ctx):
        USER_ID = ctx.message.author.id
        USER_NAME = str(ctx.message.author)
        SQL.execute('create table if not exists Accounts("Num" integer primary key autoincrement,"user_name" text, "user_id" integer not null, "balance" real)')
        SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
        result_userID = SQL.fetchone()

        if result_userID is None:
            SQL.execute('insert into Accounts(user_name, user_id, balance) values(?,?,?)', (USER_NAME, USER_ID, START_BALANCE))
            db.commit()

        SQL.execute(f'select balance from Accounts where user_id="{USER_ID}"')
        result_userbal = SQL.fetchone()
        await ctx.send(f"{ctx.message.author.mention} has a balance of {result_userbal[0]} {C_NAME}")


    @commands.command(pass_context=True, brief="Pay Someone", aliases=["pay", "give"])
    async def transfer(self, ctx, other: discord.Member, amount: int):
        USER_ID = ctx.message.author.id
        USER_NAME = str(ctx.message.author)
        OTHER_ID = other.id
        OTHER_NAME = str(other)

        SQL.execute('create table if not exists Accounts("Num" integer primary key autoincrement,"user_name" text, "user_id" integer not null, "balance" real)')
        SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
        result_userID = SQL.fetchone()
        SQL.execute(f'select user_id from Accounts where user_id="{OTHER_ID}"')
        result_otherID = SQL.fetchone()

        if result_userID is None:
            SQL.execute('insert into Accounts(user_name, user_id, balance) values(?,?,?)', (USER_NAME, USER_ID, START_BALANCE))
            db.commit()
        if result_otherID is None:
            SQL.execute('insert into Accounts(user_name, user_id, balance) values(?,?,?)', (OTHER_NAME, OTHER_ID, START_BALANCE))
            db.commit()

        SQL.execute(f'select balance from Accounts where user_id="{USER_ID}"')
        result_userbal = SQL.fetchone()
        if amount > int(result_userbal[0]):
            await ctx.send(f"{ctx.message.author.mention} does not have that many {C_NAME}")
            return

        SQL.execute('update Accounts set balance = balance - ? where user_id = ?', (amount, USER_ID))
        db.commit()
        SQL.execute('update Accounts set balance = balance + ? where user_id = ?', (amount, OTHER_ID))
        db.commit()

        await ctx.send(f"{ctx.message.author.mention} sent {other.mention} {amount} {C_NAME}")

    @commands.command(pass_context=True, brief="list top 10 bank accounts", aliases=["top"])
    async def top10(self, ctx):
        SQL.execute(f"select user_name, balance from Accounts order by balance desc")
        result_top10 = SQL.fetchmany(2)

        embed = discord.Embed(
            colour=discord.Colour.orange()
        )

        embed.set_author(name="Top 10 bank accounts")
        embed.add_field(name="#1", value=f"User: {result_top10[0][0]} Bal: {result_top10[0][1]}", inline=False)
        embed.add_field(name="#2", value=f"User: {result_top10[1][0]} Bal: {result_top10[1][1]}", inline=False)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True, brief="Get some cash",)
    async def work(self, ctx, other: discord.Member, amount: int):
        USER_ID = ctx.message.author.id
        USER_NAME = str(ctx.message.author)

        SQL.execute('create table if not exists Accounts("Num" integer primary key autoincrement,"user_name" text, "user_id" integer not null, "balance" real)')
        SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
        result_userID = SQL.fetchone()

        if result_userID is None:
            SQL.execute('insert into Accounts(user_name, user_id, balance) values(?,?,?)', (USER_NAME, USER_ID, START_BALANCE))
            db.commit()

            SQL.execute(f'select balance from Accounts where user_id="{USER_ID}"')
    
            result_userbal = SQL.fetchone()
            SQL.execute('update Accounts set balance = balance + 25', (amount))
            db.commit()

            await ctx.send(f"{ctx.message.author.mention} got ${amount} dollars from work.")

            db = sqlite3.connect('main.sqlite')
            xp_credit = 2
            cursor = db.cursor()
            cursor.execute(f"SELECT user_id, exp, lvl FROM xp_leveling"
                            f"WHERE guild_id = '{message.author.guild.id}'"
                            f"AND user_id = '{message.author.id}'")
            result = cursor.fetchone()
            if result is None:
                    sql = (f"INSERT INTO xp_leveling(guild_id, user_id, exp, lvl)"
                           f"VALUES(?, ?, ?, ?)")
                    val = (message.author.guild.id, message.author.id, xp_credit, 0)
                    cursor.execute(sql, val)
                    db.commit()
            else:
                    exp = result[1] + xp_credit
                    lvl_start = result[2]
                    required_xp = math.floor(5 * (lvl_start ** 2) + 50 * lvl_start + 100)
 
        if required_xp < exp:
            lvl_start = lvl_start + 1
            await message.channel.send(f'{message.author.mention} has leveled up. Now level *{lvl_start}*')
            print('LEVEL UP')
 
            sql = "UPDATE xp_leveling SET exp = ?, lvl = ? WHERE guild_id = ? AND user_id = ?"
            val = (exp, lvl_start, str(message.author.guild.id), str(message.author.id))
            cursor.execute(sql, val)
            db.commit()

def setup(client):
    client.add_cog(Economy(client))
