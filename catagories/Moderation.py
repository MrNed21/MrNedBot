import discord
from discord.ext import commands
from discord import Member
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import time
import discord.utils

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation Ready.')
        
#Modderation ---------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, message, channel):
        """admin abuse"""
        channel = client.get_channel(channel)
        await channel.send(f' @everyone :{ctx.message.author.mention} says: {message}.')
        
#clear command to clear chat
    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        "Clears a certain amount of text before it"
        if amount <= 100:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send('cleared.')
            time.sleep(2)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send('Well lets not get carried away now!')

#kicking and banning users

    @commands.command(pass_context=True,description="Kicks the given member. Please ensure both the bot and the command invoker have the permission 'Kick Members' before running this command.")
    async def kick(self, ctx, target:discord.Member):
        """(GUILD ONLY) Boot someone outta the server. See 'ned kick' for more."""
        if not str(ctx.message.channel).startswith("Direct Message with "):
            msg=await ctx.send("Checking perms...")
            time.sleep(0.5)
            if ctx.message.guild.me.guild_permissions.kick_members:
                if ctx.message.author.guild_permissions.kick_members:
                    await ctx.send("All permissions valid, checking issues with target...")
                    time.sleep(0.5)
                    
                    if target == ctx.message.guild.owner:
                            await ctx.send("All permissions are correct, but you're attempting to kick the server owner, whom you can't kick no matter how hard you try. Whoops!")
                    else:
                        if target==ctx.message.guild.me:
                            await ctx.send("Whoops! All permissions are correct, but you just tried to make me kick myself, which is not possible. Perhaps you meant someone else, not poor me?")
                        else:
                            if target.top_role >= ctx.message.author.top_role:
                                await ctx.send("You are the same role or less than person you are trying to kick, don't bully someone your own size! :D")
                            else:
                                await ctx.send("All permissions correct, and no issues with target being self or server owner, attempting to kick.")
                                time.sleep(0.5)
                                try:
                                    await ctx.guild.kick(target)
                                    await ctx.channel.purge(limit=3)
                                    await ctx.send(":boom: BAM! ***kicc'd***")
                                except Exception:
                                    await ctx.channel.purge(limit=3)
                                    await ctx.send("I was unable to kick the passed member. The member may have a higher role than me, I may have crashed into a rate-limit, or an unknown error may have occured. In that case, try again. Or who knows? I might be a stupid fuck who cant do my job.")
                else:
                    await ctx.channel.purge(limit=3)
                    await ctx.send("I've the correct permissions, {}, but you do not. Perhaps ask for them?").format(ctx.message.author.mention)
            else:
                await ctx.channel.purge(limit=3)
                await ctx.send("I'm just a poor bot with no permissions. Could you kindly grant me the permission `Kick Members`? Thanks! :slight_smile:")
        else:
            await ctx.send("'Tis a DM! This command is for servers only... try this again in a server maybe? :slight_smile:")


    @commands.command(pass_context=True,description="Bans the given member. Please ensure both the bot and the command invoker have the permission 'Ban Members' before running this command.")
    async def ban(self, ctx, target:discord.Member):
        """(GUILD ONLY) Ban someone outta the server. See 'ned ban' for more."""
        if not str(ctx.message.channel).startswith("Direct Message with "):
            msg=await ctx.send("Checking perms...")
            time.sleep(0.5)
            if ctx.message.guild.me.guild_permissions.ban_members:
                if ctx.message.author.guild_permissions.ban_members:
                    await ctx.send("All permissions valid, checking issues with target...")
                    time.sleep(0.5)
                    if target == ctx.message.guild.owner:
                            await ctx.send("All permissions are correct, but you're attempting to ban the server owner, whom you can't ban no matter how hard you try. Whoops!")
                    else:
                        if target == ctx.message.guild.me:
                            await ctx.send("Whoops! All permissions are correct, but you just tried to make me ban myself, which is not possible. Perhaps you meant someone else, not poor me?")
                        else:
                            if target.top_role >= ctx.author.top_role:
                                await ctx.send("You are the same role or less than the person you are trying to ban, don't bully someone your own size! :D")
                            else:
                                await ctx.send("All permissions correct, and no issues with target being self or server owner, attempting to ban.")
                                time.sleep(0.5)
                                try:
                                    await ctx.guild.ban(target)
                                    await ctx.channel.purge(limit=3)
                                    await ctx.send(":boom: BAM! ***bann'd*** https://tenor.com/view/blob-banned-ban-hammer-blob-ban-emoji-gif-16021044")
                                except Exception:
                                    await ctx.channel.purge(limit=3)
                                    await ctx.send("I was unable to ban the passed member. The member may have a higher role than me, I may have crashed into a rate-limit, or an unknown error may have occured. In that case, try again. Or who knows? I might be a stupid fuck who cant do my job.")
                else:
                    await ctx.channel.purge(limit=3)
                    await ctx.send("I've the correct permissions, {}, but you do not. Perhaps ask for them?").format(ctx.message.author.mention)
            else:
                await ctx.channel.purge(limit=3)
                await ctx.send("I'm just a poor bot with no permissions. Could you kindly grant me the permission `Ban Members`? Thanks! :slight_smile:")
        else:
            await ctx.send("'Tis a DM! This command is for servers only... try this again in a server maybe? :slight_smile:")

#pulls names of banned users to unban them
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        "reset the ban of a user"
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                try:
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                    return
                except Exception:
                    await ctx.send('You do not have the perms, or that member is not banned.')

    @commands.command(pass_context=True,description="Mue the given member. Please ensure both the bot and the command invoker have the permission 'Ban Members' before running this command.")
    async def mute(self, ctx, target:discord.Member, * role: discord.Role):
        """(GUILD ONLY) shut someone up. See 'ned mute' for more."""
        if not str(ctx.message.channel).startswith("Direct Message with "):
            msg=await ctx.send("Checking perms...")
            time.sleep(0.5)
            if ctx.message.guild.me.guild_permissions.ban_members:
                if ctx.message.author.guild_permissions.ban_members:
                    await ctx.send("All permissions valid, checking issues with target...")
                    time.sleep(0.5)
                    if target == ctx.message.guild.owner:
                            await ctx.send("All permissions are correct, but you're attempting to mute the server owner, who I think would be very mad if you did. Whoops!")
                    else:
                        if target == ctx.message.guild.me:
                            await ctx.send("Whoops! All permissions are correct, but you just tried to make me mute myself, which is not possible. Perhaps you meant someone else, not poor me?")
                        else:
                            if target.top_role >= ctx.author.top_role:
                                await ctx.send("You are the same role or less than the person you are trying to mute, don't bully someone your own size! :D")
                            else:
                                await ctx.send("All permissions correct, and no issues with target being self or server owner, attempting to mute.")
                                time.sleep(0.5)
                                try:
                                    role = discord.utils.get(ctx.guild.roles, name='Muted')
                                    await member.add_roles(role)
                                    await ctx.channel.purge(limit=3)
                                    await ctx.send(f'Muted {ctx.message.target.mention}')
                                except Exception:
                                    await ctx.channel.purge(limit=3)
                                    await ctx.send("I was unable to mute the passed member. The member may have a higher role than me, I may have crashed into a rate-limit, or an unknown error may have occured. In that case, try again. Or who knows? I might be a stupid fuck who cant do my job.")
                else:
                    await ctx.channel.purge(limit=3)
                    await ctx.send("I've the correct permissions, but you do not. Perhaps ask for them?").format(ctx.message.author.mention)
            else:
                await ctx.channel.purge(limit=3)
                await ctx.send("I'm just a poor bot with no permissions. Could you kindly grant me the permission `Manage Roles`? Thanks! :slight_smile:")
        else:
            await ctx.send("'Tis a DM! This command is for servers only... try this again in a server maybe? :slight_smile:")
                                    
    @commands.command(pass_context=True,description="Unmutes the given member. Please ensure both the bot and the command invoker have the permission 'Manage Roles' before running this command.")
    async def unmute(self, ctx, target:discord.Member, * role: discord.Role):
        """(GUILD ONLY) Ban someone outta the server. See 'ned unmute' for more."""
        if not str(ctx.message.channel).startswith("Direct Message with "):
            msg=await ctx.send("Checking perms...")
            time.sleep(0.5)
            if ctx.message.guild.me.guild_permissions.manage_roles:
                if ctx.message.author.guild_permissions.manage_roles:
                    await ctx.send("All permissions valid, checking issues with target...")
                    time.sleep(0.5)
                    if target.top_role >= ctx.author.top_role:
                        await ctx.send("You are the same role or less than the person you are trying to unmute, you can't save them! >:D")
                    else:
                                await ctx.send("All permissions correct, attempting to unmute.")
                                time.sleep(0.5)
                                try:
                                    role = discord.utils.get(ctx.guild.roles, name="Muted")
                                    await target.remove_roles(role)
                                    await ctx.channel.purge(limit=3)
                                    await ctx.send(f'Unmuted {ctx.message.target.mention}')
                                except Exception:
                                    await ctx.channel.purge(limit=4)
                                    await ctx.send("I was unable to unmute the passed member. The member may have a higher role than me, I may have crashed into a rate-limit, or an unknown error may have occured. In that case, try again. Or who knows? I might be a stupid fuck who cant do my job.")
                else:
                    await ctx.channel.purge(limit=4)
                    await ctx.send("I've the correct permissions, {}, but you do not. Perhaps ask for them?").format(ctx.message.author.mention)
            else:
                await ctx.channel.purge(limit=4)
                await ctx.send("I'm just a poor bot with no permissions. Could you kindly grant me the permission `Manage Roles`? Thanks! :slight_smile:")
        else:
            await ctx.send("'Tis a DM! This command is for servers only... try this again in a server maybe? :slight_smile:")


   
def setup(client):
    client.add_cog(Mod(client))
