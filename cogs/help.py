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
        em.add_field(name = "`;bible`", value = "gebruik `;bible` voor de link naar de Real Official Bible", inline=False)             
        em.add_field(name = "`;sw`", value = "gebruik `;sw`, `;starwars` voor starwars quotes", inline=False)
        em.add_field(name = "`;q`", value = "gebruik `;q`, `;quotes` voor official sexy quotes", inline=False)
        em.add_field(name = "`;bans`", value = "gebruik `;bans` om de bans te bekijken!", inline=False)
        em.add_field(name = "`;banaan`", value = "gebruik `;banaan`, `;bananen` om foto's te krijgen van Chris de banaan", inline=False)
        em.add_field(name = "`;8ball`", value = "gebruik `;8ball`, `;ball` om een vraag te stellen aan de magische 8 bal", inline=False)
        em.add_field(name = "`;kanker`", value = "gebruik `;kanker`, `;kkr` om iemand de kanker toe te wensen", inline=False)
        em.add_field(name = "`;dis`", value = "gebruik `;dis`, `;discriminatie` als je je gediscrimineert voelt", inline=False)
        em.add_field(name= "Links", value = "Sourcecode: [Github](https://github.com/Smikkel20/RealOfficialBot)", inline=False)
        em.set_footer(text="Send by the real official bot", icon_url="https://media.discordapp.net/attachments/798901280092454943/824375361365475368/image0.png")
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Helpcommand(bot))
    print("Help has been loaded")