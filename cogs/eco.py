import discord
import os
import random
import json
import sys
sys.path.append("./")
from globalfunc import open_account, get_bank_data, skill_lvlup, lvlup, update_bank
from discord.ext.commands import Bot
from discord.ext import commands

class Eco(commands.Cog):
    
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
    
    @commands.command(aliases = ["give"])
    async def _give(self, ctx, give = 0, user:discord.Member = None):
        if ctx.author.id != 335427967490588672:
            await ctx.send("Only Smikkel20 can give people money")
            return
        if user == None:
            user = ctx.author

        open_account(user)
        users = get_bank_data()

        update_bank(user, give)

        await ctx.send(f"succesfully gave {user.mention} {give} eendheid")



    @commands.command(aliases = ["b", 'bal', 'balance'])
    async def _bal(self, ctx, user:discord.Member = None):
        if user == None:
            user = ctx.author

        open_account(user)
        users = get_bank_data()

        bal_user = users[str(user.id)]["bal"]
        em = discord.Embed(title = f"{user.name}'s balance", color=discord.Color.blue())
        em.add_field(name = "Balance", value = bal_user)
        await ctx.send(embed = em)
    
    @commands.command(aliases = ["lvl", "level", "l"])
    async def _lvl(self, ctx, user:discord.Member = None):
        if user == None:
            user = ctx.author

        open_account(user)
        users = get_bank_data()

        userdata = users[str(user.id)]
        skills = users[str(user.id)]["Skills"]

        #overall lvl
        userlvl = userdata["lvl"]
        userlvlprog = userdata["lvlprogress"]

        #pickpocket skill
        pick_skill_lvl = skills["pickpocketskill"]["lvl"]
        pick_skill_prog = skills["pickpocketskill"]["lvlprogress"]

        #lockpick skill
        lock_skill_lvl = skills["lockpickskill"]["lvl"]
        lock_skill_prog = skills["lockpickskill"]["lvlprogress"]

        em = discord.Embed(title = f"{user.name} [{userlvl}]", description = f"Experience - {round(userlvlprog)}/{round(100 * (userlvl**1.5))}", color=discord.Color.blue())
        em.add_field(name = f"Pickpocket Skill [{pick_skill_lvl}]", value = f"Experience - {round(pick_skill_prog)}/{round(100 * (pick_skill_lvl**1.5))}", inline=True)
        em.add_field(name = f"Lockpick Skill [{lock_skill_lvl}]", value = f"Experience - {round(lock_skill_prog)}/{round(100 * (lock_skill_lvl**1.5))}", inline=True)
        em.add_field(name = f"Placeholder Skill [{pick_skill_lvl}]", value = f"Experience - {round(pick_skill_prog)}/{round(100 * (pick_skill_lvl**1.5))}", inline=True)

        await ctx.send(embed = em)

    @commands.command(aliases = ["pickpocket", "pick"])

    async def _pick(self, ctx):
        open_account(ctx.author)
        user = ctx.author

        pick = random.randint(1, 100)

        users = get_bank_data()
        skill = "pickpocketskill"
        boost= users[str(user.id)]["Skills"]["pickpocketskill"]["boost"]
        print(boost)
        chance = 100-boost

        if pick <= chance:
            pick = -10
            em = discord.Embed(description = f"Iemand zag je stelen en je ontvangt een boete van {pick-pick-pick} eendheid!" ,color = discord.Color.blue())
            await ctx.send(embed = em)
            xp = 10
        else:
            pick == pick * users[str(user.id)]["Skills"]["pickpocketskill"]["lvl"]
            em = discord.Embed(description = f"Je hebt {pick} eendheid gestolen!" ,color = discord.Color.blue())
            await ctx.send(embed = em)
            xp = 50
        
        await lvlup(ctx, ctx.author, xp)
        await skill_lvlup(ctx, ctx.author, skill, xp)
        update_bank(ctx.author, pick)
    
    @commands.command(aliases = ["steal"])
    async def _steal(self, ctx):
        stolen = random.randint(1, 100)
        if stolen <= 50:
            em = discord.Embed(description = "Iemand zag je stelen en je ontvangt een boete van 50 eendheid!" ,color = discord.Color.blue())
            await ctx.send(embed = em)
            stolen = -50
        else:
            em = discord.Embed(description = f"Je hebt {stolen} eendheid gestolen!" ,color = discord.Color.blue())
            await ctx.send(embed = em)
        update_bank(ctx.author, stolen)




    

def setup(bot):
    bot.add_cog(Eco(bot))
    print("Eco has been loaded")