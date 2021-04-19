import discord
import os
import random
import json
import sys
sys.path.append("./")
from globalfunc import open_account, get_bank_data, skill_lvlup, lvlup, update_bank
from discord.ext.commands import Bot
from discord.ext import commands

bmshop = [{"id":"001","name":"Weed","price":10,"description":"The good stuff"},
          {"id":"002","name":"Lockpick","price":100,"description":"Met een lockpick kun je de lock van een huis open krijgen."},
          {"id":"003","name":"Strong Lock","price":100000,"description":"Om je lockpicking skill te oefenen"}]


class bm(commands.Cog):
    
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot


    @commands.command(aliases = ["bm", "blackmarket"])
    async def _bm(self, ctx):
        open_account(ctx.author)
        user = ctx.author
        users = get_bank_data()

        em = discord.Embed(title = "Black Market", description = "Welkom bij de zwarte markt waar je alle illegale spullen kunt kopen, gebruik `;buy <id> <amount>` om iets te kopen.")

        for item in bmshop:
            ID = item["id"]
            name = item["name"]
            price = item["price"]
            desc = item["description"]
            em.add_field(name = f"[{ID}]{name}", value = f"{desc}——Price: {price}")
        
        await ctx.send(embed = em)

    @commands.command(aliases = ["buy"])
    async def _buy(self, ctx, ID=None, amount=1):
        open_account(ctx.author)
        user = ctx.author
        users = get_bank_data()

        userbal = users[str(user.id)]["bal"]

        if ID == None:
            em = discord.Embed(description = "gebruik `;buy <id> <amount>` om iets te kopen",color = discord.Color.blue())
        else:

            for item in bmshop:
                if item["id"] == ID:
                    price = item["price"]
                    name = item["name"]
                    break
                name = None
            
            if name == None:
                await ctx.send("Geef een bestaand id op")
                return
            name = name.lower()
            
            if ID == "003":
                lockpickitem = users[str(user.id)]["Skills"]["LockpickSkill"]["trainitem"]
                if lockpickitem == True:
                    await ctx.send(f"Je hebt de {name} al gekocht, gebruik `;train lockpick` om hem te gebruiken.")
                    return
                else:
                    users[str(user.id)]["bal"] -= price
                    users[str(user.id)]["Skills"]["LockpickSkill"]["trainitem"] = True
                    em = discord.Embed(description = f"Je hebt succesvol een {name} gekocht, gebruik `;train lockpick` om hem te gebruiken.",color = discord.Color.blue())
            else:

                if amount <= 0:
                    await ctx.send(f"Je kan niet minder dan 0 {name} kopen")
                    return
            
                total = price * amount

                if amount == 1:
                    more = ""
                else:
                    more = "'s"
                if ID == "001":
                    more = ""

                if userbal < total:
                    await ctx.send(f"Je hebt ten minste {total} eendheid nodig om {amount} {name}{more} te kopen")
                    return

                users[str(user.id)]["bal"] -= total
                users[str(user.id)]["items"][name] += amount

                em = discord.Embed(description = f"Je hebt succesvol {amount} {name}{more} gekocht voor {total} eendheid.",color = discord.Color.blue())

        with open("mainbank.json","w") as f:
            json.dump(users,f)
        await ctx.send(embed = em)
        


def setup(bot):
    bot.add_cog(bm(bot))
    print("bm has been loaded")