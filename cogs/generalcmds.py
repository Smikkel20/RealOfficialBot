import discord
import os
import random
import json
import requests
import io
import sys
from bs4 import BeautifulSoup
from discord.ext.commands import Bot, bot
from discord.ext import commands

with open("txt/quotes.txt", "r") as q:
    quotes = []
    for line in q:
        line = line.strip()
        if line:
            quotes.append(line)

with open("txt/quotes2.txt", "r") as q:
    quotes2 = []
    for line in q:
        line = line.strip()
        if line:
            quotes2.append(line)
            
with open("txt/responses.txt", "r") as q:
    responses = []
    for line in q:
        line = line.strip()
        if line:
            responses.append(line)

with open("txt/banaan.txt", "r") as q:
    banaan = []
    for line in q:
        line = line.strip()
        if line:
            banaan.append(line)

def quotes2_reload():
    with open("txt/quotes2.txt", "r") as q:
        quotes2 = []
        for line in q:
            line = line.strip()
            if line:
                quotes2.append(line)
    print("done")    

class cmds(commands.Cog):
    
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
    
    @commands.command(aliases = ["arda"])
    async def _arda(self, ctx):
        URL = "http://api.roblox.com/users/1455250581/onlinestatus"
        page = requests.get(URL)
        data = page.json()
        if data["IsOnline"] == True:
            status = "online"
        else:
            status = "offline"

        em = discord.Embed(title = "Arda strijder", description = f"[Arda](https://www.roblox.com/users/1455250581/profile) is op dit moment **{status}**", color = discord.Color.blue())
        await ctx.send(embed = em)
    
    @commands.command(aliases = ["discriminatie", "dis"])
    async def _dis(self, ctx, user:discord.Member = None):
        if user == None:
            em = discord.Embed(description = f"{ctx.author.mention} voelt zich gediscrimineert",color = discord.Color.blue())
        elif user.id == self.bot.user.id:
            em = discord.Embed(description = f"Hoe kan ik jou nou hebben gediscrimineert",color = discord.Color.blue())
        else:
            em = discord.Embed(description = f"{ctx.author.mention} voelt zich gediscrimineert door {user.mention}",color = discord.Color.blue())
        await ctx.send(embed = em)
    
    @commands.command(aliases = ["kanker", "kkr"])
    async def _kanker(self, ctx, user:discord.Member = None):
        if user == None:
            em = discord.Embed(description = f"{ctx.author.mention} gebruikt de move **KANKER**!",color = discord.Color.blue())
        elif user.id == self.bot.user.id:
            em = discord.Embed(description = f"KRIJG ZELF DE KANKER!",color = discord.Color.blue())
        else:
            em = discord.Embed(description = f"{user.mention} krijgt kanker toegewenst door {ctx.author.mention}",color = discord.Color.blue())
        await ctx.send(embed = em)

    @commands.command(aliases = ["banaan", "bananen", "banan"])
    async def _banaan(self, ctx):
        photo = random.choice(banaan)
        
        em = discord.Embed(color = discord.Color.blue())
        em.set_image(url=f"{photo}")
        em.set_footer(text="Send by the real official bot", icon_url="https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png")

        await ctx.send(embed = em)

    @commands.command(aliases = ["bans"])
    async def _bans(self,ctx):
        URL = "https://docs.google.com/document/d/1IqqL4FtKwvp9mmO2QAljmAGeadSCI2bu1C7W-OSXwig/edit"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all("script", type='text/javascript')

        with io.open("txt/html.txt", "w", encoding="utf-8") as f:
            f.write(str(results))
            f.close

        f = io.open("txt/html.txt", "r", encoding="utf-8")
        File = str(f.read())
        people = []
        number = 0

        for i in File.split("u001c"):
            number += 1
            if number % 2 == 0:
                i = i[:-3]
                people.append(i)
            else:
                if "u003d" in i:
                    i = i.replace("u003d", "=")
                if "u003c3" in i:
                    i = i.replace("u003c3", "<3")
                if "u003e" in i:
                    i = i.replace("u003e", ">")
                i = i[:-9]
                people.append(i)

        people = people[1:]
        last = people[-1]
        number = 0

        for i in last.split("n"):
            if number == 0:
                people[-1] = i[:-1]
            number += 1

        number = 0
        em = discord.Embed(title="BANS",color=discord.Color.blue())
        for i in people:
            number += 1
            if number % 2 == 0:
                Number = i
                em.add_field(name= name ,value= f"{name} - {Number}", inline=False)
            else:
                name = i
        await ctx.send(embed = em)        
            
    @commands.command(aliases = ["swquotes", "starwars", "starwarsquotes", "sw", "swq"])
    async def _sw(self, ctx):
        quote = random.choice(quotes)

        em = discord.Embed(description = f"{quote}" ,color = discord.Color.blue())
        
        await ctx.send(embed = em)
        if quote == "Hello There.":
            em = discord.Embed(description = f"General Kenobi." ,color = discord.Color.red())
            await ctx.send(embed = em)
    
    @commands.command(aliases = ["quote", "quotes", "q", "rq"])
    async def _quote(self, ctx):
        quote = random.choice(quotes2)
        
        em = discord.Embed(description = f"{quote}" ,color = discord.Color.blue())
        
        await ctx.send(embed = em)

    @commands.command(aliases = ["8ball", "ball", "bal", "8bal"])
    async def _8ball(self, ctx, *, question):
        response = random.choice(responses)

        embed=discord.Embed(title="De Magische 8 Bal Heeft Gesproken!", color = discord.Color.blue())
        embed.add_field(name='Vraag: ', value=f'{question}', inline=True)
        embed.add_field(name='Antwoord: ', value=f'{response}', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(cmds(bot))
    print("General commands has been loaded!")
