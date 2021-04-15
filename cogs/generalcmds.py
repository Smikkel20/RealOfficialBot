import discord
import os
import random
import json
from discord.ext.commands import Bot
from discord.ext import commands

with open("quotes.txt", "r") as q:
    quotes = []
    for line in q:
        line = line.strip()
        if line:
            quotes.append(line)
    
    q.close

with open("quotes2.txt", "r") as q:
    quotes2 = []
    for line in q:
        line = line.strip()
        if line:
            quotes2.append(line)

class cmds(commands.Cog):
    
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(aliases = ["swquotes", "starwars", "starwarsquotes", "sw"])
    async def _sw(self, ctx):
        quote = random.choice(quotes)
        
        em = discord.Embed(description = f"{quote}" ,color = discord.Color.blue())

        await ctx.send(embed = em)
    
    @commands.command(aliases = ["quote", "quotes", "q", "rq"])
    async def _quote(self, ctx):
        quote = random.choice(quotes2)
        
        em = discord.Embed(description = f"{quote}" ,color = discord.Color.blue())

        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(cmds(bot))
    print("General commands has been loaded")