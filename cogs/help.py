import discord
import os
import random
from discord.ext.commands import Bot
from discord.ext import commands

class Helpcommand(commands.Cog):
    
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
    
    #Creates subcommand for help
    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(title = "Help", color = discord.Color.blue())
        em.add_field(name = "`;bible`", value = "use `;bible` to get a link to the official bible", inline=False)             
        em.add_field(name = "`;sw`", value = "use `;sw`, `;starwars` for starwars quotes", inline=False)
        em.add_field(name = "`;q`", value = "use `;q`, `;quotes` for official sexy quotes", inline=False)
        em.add_field(name = "`;bans`", value = "use `;bans` to see how many bans everyone has!", inline=False)
        em.add_field(name = "`;banaan`", value = "use `;banaan`, `;bananen` to get photos of a beautyfull banana!", inline=False)
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Helpcommand(bot))
    print("Help has been loaded")