import os
import discord
import sys
import random
from globalfunc import open_account, get_bank_data, skill_lvlup, lvlup, update_bank
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive

bot = commands.Bot(command_prefix = ";", case_insensitive = True)
bot.remove_command("help")

with open("txt/seks.txt", "r") as q:
    seks = []
    for line in q:
        line = line.strip()
        if line:
            seks.append(line)

if __name__ == "__main__":
    #get every file in ./cogs dir
    for filename in os.listdir("./cogs"):
        #check if the filename ends with .py
        if filename.endswith(".py"):
            try:
                #load <filename>
                bot.load_extension(f"cogs.{filename[:-3]}")
            except Exception as e:
                print(f"failed to load extension {filename}", file=sys.stderr)

load_dotenv()
#get tokens from .env file
TOKEN = os.getenv("TEST_TOKEN")

@bot.event
async def on_ready():
    print("---------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    #Sets activity 
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The real official bible", url="https://docs.google.com/document/d/1IqqL4FtKwvp9mmO2QAljmAGeadSCI2bu1C7W-OSXwig/edit?usp=drivesdk"))
    print('activity set')
    print('---------------')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        return
    else:
        raise error

@bot.event
async def on_message(ctx):
    message = str(ctx.content)
    if ctx.author.bot:
        return
    open_account(ctx.author)
    users = get_bank_data()
    try:
        if ctx.channel.name == 'super-secret-quotes':
            with open("txt/quotes2.txt", "a") as q:
                q.write(f"{message}\n")
                q.close
                for filename in os.listdir("./cogs"):
                    if filename.endswith("generalcmds.py"):
                        #reload extensions
                        bot.unload_extension(f"cogs.{filename[:-3]}")
                        bot.load_extension(f"cogs.{filename[:-3]}")
    except AttributeError:
        dm = True

    if "hoe werkt seks" in message.lower():
        text = random.choice(seks)
        getal = random.randint(1,100)
        if getal == 1:
            em = discord.Embed(description = f"Waar ben ik toch ook mee bezig." ,color = discord.Color.red())
        else:
            em = discord.Embed(description = f"{text}" ,color = discord.Color.red())
        await ctx.channel.send(embed = em)

    if "hello there" in message.lower():
        em = discord.Embed(description = f"General Kenobi." ,color = discord.Color.red())
        await ctx.channel.send(embed = em)
        em = discord.Embed(description = f"You are a blod one." ,color = discord.Color.red())
        await ctx.channel.send(embed = em)
    await bot.process_commands(ctx)

@bot.command()
async def bible(ctx):
    em = em = discord.Embed(
        name = "The real official bible",
        description = f"[The real official bible](https://docs.google.com/document/d/1IqqL4FtKwvp9mmO2QAljmAGeadSCI2bu1C7W-OSXwig/edit?usp=drivesdk)" ,color = discord.Color.red())
    
    await ctx.send(embed = em)

@bot.command()
async def ping(ctx):
    await ctx.send(
        f'Pong! {round(bot.latency, 2)} ms!')

#@bot.command()
#async def reload(ctx):
#    for filename in os.listdir("./cogs"):
#        if filename.endswith(".py"):
#            try:
#                #reload extensions
#                bot.unload_extension(f"cogs.{filename[:-3]}")
#                bot.load_extension(f"cogs.{filename[:-3]}")
#                await ctx.send(f"Reloaded {filename[:-3]}")
#            except Exception as e:
#                print(f"failed to reload extension cogs.{filename[:-3]}", file=sys.stderr)




keep_alive()
bot.run(TOKEN)