import discord
from discord.ext import commands
from discord.utils import get
import os
from discord.ext.commands import has_permissions, MissingPermissions
import json
import asyncio

bot = commands.Bot(command_prefix=".")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)
    await bot.change_presence(activity=discord.Game(name="Här kan det stå vad du vill!"))

@bot.event
async def on_member_join(member):
    unverified = discord.utils.get(member.guild.roles, name="lvl1") #finds the unverified role in the guild
    await member.add_roles(unverified) #adds the unverified role to the member
    

def channel_2(ctx):
    return ctx.channel.id == 871066907766325309

@bot.command()
@commands.check(channel_2) # checks if the channel the command is being used in is the verifiy channel
async def verify(ctx, user: discord.Member=None):
    unverified = discord.utils.get(ctx.guild.roles, name="lvl1") #finds the unverified role in the guild
    if unverified in ctx.author.roles: #checks if the user running the command has the unveirifed role
        verify = discord.utils.get(ctx.guild.roles, name="lvl2") #finds the verified role in the guild

        await ctx.message.delete()     
        await ctx.author.remove_roles(unverified)
        await ctx.author.add_roles(verify) #adds the verified role to the member
        await ctx.author.send("Du har nu tillgång till lvl2! ✅")
    else:
        await ctx.message.delete()  
        await ctx.author.send('Du är redan lvl2 eller högre! ❎')







bot.run(os.environ['TOKEN'])