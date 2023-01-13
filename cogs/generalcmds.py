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
from discord import app_commands

chantal = [
    "https://cdn.discordapp.com/attachments/695690532633968691/918177532833058816/IMG_0573.png",
    "https://cdn.discordapp.com/attachments/695690532633968691/918050011919556628/IMG_3993.jpg",
    "https://cdn.discordapp.com/attachments/695690532633968691/918090365251256360/IMG_3997.jpg",
    "https://cdn.discordapp.com/attachments/831455559211155476/915265130579759144/IMG_3738.png",
    "https://cdn.discordapp.com/attachments/695690532633968691/918230798203764907/CHANTALL.png",
    "https://cdn.discordapp.com/attachments/831455559211155476/915265130290380820/IMG_3766.webp",
    "https://cdn.discordapp.com/attachments/693545511151599640/915924335783473192/IMG_3849.jpg",
    "https://cdn.discordapp.com/attachments/794667484367683604/917815028982353941/IMG_3987.png",
    "https://cdn.discordapp.com/attachments/695690532633968691/917836728881012736/3DFA8DBC-098D-4D49-A04D-A62AF7F3103E.jpg",
    "https://cdn.discordapp.com/attachments/831455559211155476/917873234316263434/E291B4F6-27D6-41D6-932B-1F7BB58B70E0.jpg",
    "https://media.discordapp.net/attachments/794667484367683604/922606711657889823/IMG_4789.png?width=1440&height=665"
]
zelfmoord_text = [
    "heeft er geen zin meer in.", "heeft leven opgegeven",
    "chooses the easy way out!", "pleegt Zelfmoord",
    "ziet het niet meer zitten", "wil dood", "kills themself"
]
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


def robert_reload():
    with open("txt/robert.txt", "r") as q:
        robert = []
        for line in q:
            line = line.strip()
            if line:
                robert.append(line)
    print("done")


class cmds(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.hybrid_command(name="arda", with_app_command = True, description = "Leeft Arda uberhaupt nog?")
    async def _arda(self, ctx):
        URL = "http://api.roblox.com/users/1455250581/onlinestatus"
        page = requests.get(URL)
        data = page.json()
        if data["IsOnline"] == True:
            status = "online"
        else:
            status = "offline"

        em = discord.Embed(
            title="Arda strijder",
            description=
            f"[Arda](https://www.roblox.com/users/1455250581/profile) is op dit moment **{status}**",
            color=discord.Color.blue())
        await ctx.send(embed=em)

    @commands.hybrid_command(name="discriminatie", aliases=["dis"], with_app_command = True, description = "De enige echte command voor als je je gediscrimineerd voelt")
    async def _dis(self, ctx, user: discord.Member = None):
        if user == None:
            em = discord.Embed(
                description=f"{ctx.author.mention} voelt zich gediscrimineert",
                color=discord.Color.blue())
        elif user.id == self.bot.user.id:
            em = discord.Embed(
                description=f"Hoe kan ik jou nou hebben gediscrimineert",
                color=discord.Color.blue())
        else:
            em = discord.Embed(
                description=
                f"{ctx.author.mention} voelt zich gediscrimineert door {user.mention}",
                color=discord.Color.blue())
        await ctx.send(embed=em)

    @commands.hybrid_command(name="kanker", aliases=["kkr"], with_app_command = True, description = "Soms moet je gewoon even met kanker schelden, en dat mag allemaal.")
    async def _kanker(self, ctx, user: discord.Member = None):
        if user == None:
            em = discord.Embed(
                description=
                f"{ctx.author.mention} gebruikt de move **KANKER**!",
                color=discord.Color.blue())
        elif user.id == self.bot.user.id:
            em = discord.Embed(description=f"KRIJG ZELF DE KANKER!",
                               color=discord.Color.blue())
        else:
            em = discord.Embed(
                description=
                f"{user.mention} krijgt kanker toegewenst door {ctx.author.mention}",
                color=discord.Color.blue())
        await ctx.send(embed=em)

    @commands.hybrid_command(name="banaan", aliases=["bananen", "banan", "bananan"], with_app_command = True, description = "Banananchrus")
    async def _banaan(self, ctx):
        photo = random.choice(banaan)

        em = discord.Embed(color=discord.Color.blue())
        em.set_image(url=f"{photo}")
        em.set_footer(
            text="Send by the real official bot",
            icon_url=
            "https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png"
        )

        await ctx.send(embed=em)

    @commands.hybrid_command(name="rob", aliases=["robert", "robje", "bas", "basje", "Басик","Бас"], with_app_command = True, description = "Ben je Rob? Zeg het hardop")
    async def _robert(self, ctx):
        photo = random.choice(robert)

        em = discord.Embed(description="*robert*", color=discord.Color.blue())
        em.set_image(url=f"{photo}")
        em.set_footer(
            text="Send by the real official bot",
            icon_url=
            "https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png"
        )

        await ctx.send(embed=em)

    @commands.hybrid_command(name="chantal", aliases=["chant"], with_app_command = True, description = "Chantal")
    async def _chantal(self, ctx):
        photo = random.choice(chantal)
        if photo == "https://cdn.discordapp.com/attachments/794667484367683604/917815028982353941/IMG_3987.png":
            em = discord.Embed(description="**~~chantal~~ sjontal**",
                               color=discord.Color.blue())
        else:
            em = discord.Embed(description="**chantal**",
                               color=discord.Color.blue())
        em.set_image(url=f"{photo}")
        em.set_footer(
            text="Send by the real official bot",
            icon_url=
            "https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png"
        )

        await ctx.send(embed=em)

    @commands.hybrid_command(name="sjontal", with_app_command = True, description = "Sjontal")
    async def _sjontal(self, ctx):
        em = discord.Embed(description="**sjontal**",
                           color=discord.Color.blue())
        em.set_image(
            url=
            f"https://cdn.discordapp.com/attachments/794667484367683604/917815028982353941/IMG_3987.png"
        )
        em.set_footer(
            text="Send by the real official bot",
            icon_url=
            "https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png"
        )

        await ctx.send(embed=em)

    @commands.hybrid_command(name="mods", aliases=["mod"],with_app_command = True, description = "Welke mods gebruikt deze jongen nu weer, je kan het hier allemaal zien.")
    async def _mods(self, ctx):
        em = discord.Embed(
            name="Mods",
            description=
            f"[Mod list 1.19](https://drive.google.com/drive/folders/160_tAz2H9Nr_zDZ11al4yXOx9qopTPsg?usp=sharing)",
            color=discord.Color.red())

        await ctx.send(embed=em)

    @commands.hybrid_command(name="poll", aliases=["vote"], with_app_command = True, description = "Stel een vraag aan de server.")
    async def _vote(self, ctx, *, question):

        em = discord.Embed(title="Vote effe", color=discord.Color.blue())
        em.add_field(name='Vraag: ', value=f'{question}', inline=False)
        em.add_field(
            name="Antwoord:",
            value=
            "<:smikkelpog:915176741868298242> = Yea, <:distressed:853371062497968128> = Nea "
        )
        em.set_footer(
            text="Send by the real official bot",
            icon_url=
            "https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png"
        )

        message = await ctx.send(embed=em)
        await message.add_reaction(ctx.bot.get_emoji(915176741868298242))
        await message.add_reaction(ctx.bot.get_emoji(853371062497968128))
        with open("txt/poll.txt", "a") as q:
            q.write(f"{message.id}\n")
            q.close

    @commands.hybrid_command(name="bans", with_app_command = True, description = "Wie heeft onze al machtige god allemaal verbannen?")
    async def _bans(self, ctx):
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
        em = discord.Embed(title="BANS", color=discord.Color.blue())
        for i in people:
            number += 1
            if number % 2 == 0:
                Number = i
                em.add_field(name=name,
                             value=f"{name} - {Number}",
                             inline=False)
            else:
                name = i
        await ctx.send(embed=em)

    @commands.hybrid_command(name="sw", aliases=["swquotes", "starwars", "starwarsquotes", "swq"], with_app_command = True, description = "Alle prequel quotes, letterlijk allemaal.")
    async def _sw(self, ctx):
        quote = random.choice(quotes)

        em = discord.Embed(description=f"{quote}", color=discord.Color.blue())

        await ctx.send(embed=em)
        if quote == "Hello There.":
            em = discord.Embed(description=f"General Kenobi.",
                               color=discord.Color.red())
            await ctx.send(embed=em)

    @commands.hybrid_command(name="q", aliases=["quote", "quotes", "rq"], with_app_command = True, description = "De enige echte cult quotes, zelfs de klassieke.")
    async def _quote(self, ctx):
        quote = random.choice(quotes2)
        if quote == "seks123":
            em = discord.Embed(color=discord.Color.blue())
            em.set_image(
                url=
                "https://cdn.discordapp.com/attachments/794667484367683604/916066341180551228/peagle_rage_quit.png"
            )
        elif quote == "piemol123":
            em = discord.Embed(color=discord.Color.blue())
            em.set_image(
                url=
                "https://cdn.discordapp.com/attachments/700380317764288542/918253271917920256/unknown.png"
            )
        else:
            em = discord.Embed(description=f"{quote}",
                               color=discord.Color.blue())

        await ctx.send(embed=em)

    @commands.hybrid_command(name="8ball", aliases=["ball", "bal", "8bal"], with_app_command = True, description = "Vraag de almachtige 8bal een vraag")
    async def _8ball(self, ctx, *, question):
        response = random.choice(responses)

        embed = discord.Embed(title="De Magische 8 Bal Heeft Gesproken!",
                              color=discord.Color.blue())
        embed.add_field(name='Vraag: ', value=f'{question}', inline=True)
        embed.add_field(name='Antwoord: ', value=f'{response}', inline=False)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name="zelfmoord", aliases=["dood", "suicide", "death"],with_app_command = True, description = "Zelfmoord in Discord, oja en iets met 113.")
    async def _dood(self, ctx):
        zelfmoord = random.choice(zelfmoorden)
        text = random.choice(zelfmoord_text)

        em = discord.Embed(title=f"{ctx.author.name} {text}",
                           color=discord.Color.blue())
        em.set_image(url=f"{zelfmoord}")
        em.set_footer(
            text="Send by the real official bot",
            icon_url=
            "https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png"
        )

        await ctx.send(embed=em)

    @commands.hybrid_command(name="kill", aliases=["vermoord", "schiet", "shenk"], with_app_command = True, description = "Als je iemand heel graag dood wil hebben.")
    async def _kill(self, ctx, user: discord.Member = None):
        kill = random.choice(kill_)
        if ctx.author.id == user.id:
            em = discord.Embed(title=f"{ctx.author.name} pleegt zelfmoord",
                               color=discord.Color.blue())
            em.set_image(
                url=
                f"https://media.giphy.com/media/7K95K2SuBOaBaXXlGH/giphy.gif")
        elif user.id == self.bot.user.id:
            em = discord.Embed(
                title=
                f"{self.bot.user.name} vermoord {ctx.author.name} op brutale wijze",
                color=discord.Color.blue())
            em.set_image(
                url=
                f"https://media.giphy.com/media/2AY5EiMFmtU082M4nt/giphy.gif")
        else:
            em = discord.Embed(title=f"{ctx.author.name} vermoord {user.name}",
                               color=discord.Color.blue())
            em.set_image(url=f"{kill}")
        em.set_footer(
            text="Send by the real official bot",
            icon_url=
            "https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png"
        )

        await ctx.send(embed=em)

    @commands.command(aliases=["spotify", "wrapped", "spotifywrapped"])
    async def _spotify(self, ctx):
        em = discord.Embed(description="**Niemand vroeg**",
                           color=discord.Color.blue())
        em.set_image(
            url=
            f"https://cdn.discordapp.com/attachments/693545511151599640/915647354919596122/IMG_3604.png"
        )
        em.set_footer(
            text="Send by the real official bot",
            icon_url=
            "https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png"
        )

        await ctx.send(embed=em)


async def setup(bot):
    await bot.add_cog(cmds(bot))
    print("General commands has been loaded!")
