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

chantal = ["https://cdn.discordapp.com/attachments/831455559211155476/915265130579759144/IMG_3738.png",
"https://cdn.discordapp.com/attachments/831455559211155476/915265130290380820/IMG_3766.webp", "https://cdn.discordapp.com/attachments/693545511151599640/915924335783473192/IMG_3849.jpg", "https://cdn.discordapp.com/attachments/794667484367683604/917815028982353941/IMG_3987.png", "https://cdn.discordapp.com/attachments/695690532633968691/917836728881012736/3DFA8DBC-098D-4D49-A04D-A62AF7F3103E.jpg"]
zelfmoord_text = ["heeft er geen zin meer in.", "heeft leven opgegeven", "chooses the easy way out!", "pleegt Zelfmoord", "ziet het niet meer zitten", "wil dood", "kills themself"]
kill_text = []


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

with open("txt/zelfmoord.txt", "r") as q:
    zelfmoorden = []
    for line in q:
        line = line.strip()
        if line:
            zelfmoorden.append(line)

with open("txt/kill.txt", "r") as q:
    kill_ = []
    for line in q:
        line = line.strip()
        if line:
            kill_.append(line)

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

with open("txt/robert.txt", "r") as q:
    robert = []
    for line in q:
        line = line.strip()
        if line:
            robert.append(line)

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
    
    @commands.command(aliases = ["robert"])
    async def _robert(self, ctx):
        photo = random.choice(robert)
        
        em = discord.Embed(description = "*robert*", color = discord.Color.blue())
        em.set_image(url=f"{photo}")
        em.set_footer(text="Send by the real official bot", icon_url="https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png")

        await ctx.send(embed = em)
    
    @commands.command(aliases = ["chantal", "chant"])
    async def _chantal(self, ctx):
        photo = random.choice(chantal)
        
        em = discord.Embed(description = "**chantal**", color = discord.Color.blue())
        em.set_image(url=f"{photo}")
        em.set_footer(text="Send by the real official bot", icon_url="https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png")

        await ctx.send(embed = em)

    @commands.command(aliases = ["mods", "mod"])
    async def _mods(self, ctx):
        em = discord.Embed(
        name = "Mods",
        description = f"[Mod list 1.18](https://drive.google.com/drive/folders/160_tAz2H9Nr_zDZ11al4yXOx9qopTPsg?usp=sharing)" ,color = discord.Color.red())
    
        await ctx.send(embed = em)
        

    @commands.command(aliases = ["poll", "vote"])
    async def _vote(self, ctx, *,question):
        
        em = discord.Embed(Title = "Vote effe", color = discord.Color.blue())
        em.add_field(name='Vraag: ', value=f'{question}', inline=False)
        em.add_field(name = "Antwoord:", value="<:smikkelpog:915176741868298242> = Yea, <:distressed:853371062497968128> = Nea ")
        em.set_footer(text="Send by the real official bot", icon_url="https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png")

        message = await ctx.send(embed = em)
        await message.add_reaction(emoji="<:smikkelpog:915176741868298242>")
        await message.add_reaction(emoji="<:distressed:853371062497968128>")
        with open("txt/poll.txt", "a") as q:
                q.write(f"{message.id}\n")
                q.close

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
        if quote == "seks123":
            em = discord.Embed(color = discord.Color.blue())
            em.set_image(url="https://cdn.discordapp.com/attachments/794667484367683604/916066341180551228/peagle_rage_quit.png")
        else:
            em = discord.Embed(description = f"{quote}" ,color = discord.Color.blue())
        
        await ctx.send(embed = em)

    @commands.command(aliases = ["8ball", "ball", "bal", "8bal"])
    async def _8ball(self, ctx, *, question):
        response = random.choice(responses)

        embed=discord.Embed(title="De Magische 8 Bal Heeft Gesproken!", color = discord.Color.blue())
        embed.add_field(name='Vraag: ', value=f'{question}', inline=True)
        embed.add_field(name='Antwoord: ', value=f'{response}', inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(aliases = ["dood", "zelfmoord", "suicide", "death"])
    async def _dood(self, ctx):
        zelfmoord = random.choice(zelfmoorden)
        text = random.choice(zelfmoord_text)

        em = discord.Embed(title = f"{ctx.author.name} {text}" ,color = discord.Color.blue())
        em.set_image(url=f"{zelfmoord}")
        em.set_footer(text="Send by the real official bot", icon_url="https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png")

        await ctx.send(embed = em)

    @commands.command(aliases = ["kill", "vermoord", "schiet", "shenk"])
    async def _kill(self, ctx, user:discord.Member = None):
        kill = random.choice(kill_)
        if ctx.author.id == user.id:
          em = discord.Embed(title = f"{ctx.author.name} pleegt zelfmoord" ,color = discord.Color.blue())
          em.set_image(url=f"https://media.giphy.com/media/7K95K2SuBOaBaXXlGH/giphy.gif")
        elif user.id == self.bot.user.id:
          em = discord.Embed(title = f"{self.bot.user.name} vermoord {ctx.author.name} op brutale wijze" ,color = discord.Color.blue())
          em.set_image(url=f"https://media.giphy.com/media/2AY5EiMFmtU082M4nt/giphy.gif")
        else:
          em = discord.Embed(title = f"{ctx.author.name} vermoord {user.name}" ,color = discord.Color.blue())
          em.set_image(url=f"{kill}")
        em.set_footer(text="Send by the real official bot", icon_url="https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png")

        await ctx.send(embed = em)



def setup(bot):
    bot.add_cog(cmds(bot))
    print("General commands has been loaded!")
