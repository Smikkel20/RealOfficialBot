import discord
import os
import random
import sys
sys.path.append("./")
from globalfunc import open_account, get_bank_data, skill_lvlup, lvlup, update_bank
from discord.ext.commands import Bot
from discord.ext import commands

class Skill(commands.Cog):
    
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands .command(aliases = ["train", "t"])
    async def _train(self, ctx, skill = None):
        open_account(ctx.author)
        user = ctx.author
        users = get_bank_data()

        user_lvl = users[str(user.id)]["lvl"]

        if skill == None:
            em = discord.Embed(description = "gebruik `;train <skill>` om te trainen, de skills die je kan trainen zijn `lockpick`,",color = discord.Color.blue())
        else:
            TrainSkill = users[str(user.id)]["Skills"]
            for Skill in TrainSkill:
                if Skill == f"{skill}skill":
                    try:
                        item = users[str(user.id)]["Skills"][Skill]["trainitem"]
                    except KeyError:
                        item = None
                    lvl = users[str(user.id)]["Skills"][Skill]["lvl"]
                    break
                item = None
            
            if item == None:
                await ctx.send("Geef een skill op die je kan trainen zoals `lockpick`")
                return
            
            if item == False:
                await ctx.send(f"Je hebt de train item voor `{skill}` om deze skill te trainen.")
                return
            
            xp = (50 * ((lvl + user_lvl) // 2))**1.05

            em = discord.Embed(description = f"Je hebt succesvol {round(xp)} xp gekregen door het trainen van je {skill} skill",color = discord.Color.blue())

            await lvlup(ctx, ctx.author, xp)
            await skill_lvlup(ctx, ctx.author, Skill, xp)
        await ctx.send(embed = em)




def setup(bot):
    bot.add_cog(Skill(bot))
    print("Skill has been loaded")