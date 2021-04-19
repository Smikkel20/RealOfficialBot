import discord
import os
import random
import json
from discord.ext.commands import Bot
from discord.ext import commands

def open_account(user):
    users = get_bank_data()
    
    if str(user.id) in users:
        return
    else:
        #creating all there account variables
        users[str(user.id)] = {}
        users[str(user.id)]["bal"] = 0
        users[str(user.id)]["lvl"] = 1
        users[str(user.id)]["lvlprogress"] = 0
        #user skills
        users[str(user.id)]["Skills"] = {}
        users[str(user.id)]["Skills"]["pickpocketskill"] = {}
        users[str(user.id)]["Skills"]["pickpocketskill"]["lvl"] = 1
        users[str(user.id)]["Skills"]["pickpocketskill"]["lvlprogress"] = 0
        users[str(user.id)]["Skills"]["pickpocketskill"]["boost"] = 5
        users[str(user.id)]["Skills"]["lockpickskill"] = {}
        users[str(user.id)]["Skills"]["lockpickskill"]["lvl"] = 1
        users[str(user.id)]["Skills"]["lockpickskill"]["lvlprogress"] = 0
        users[str(user.id)]["Skills"]["lockpickSkill"]["boost"] = 5
        users[str(user.id)]["Skills"]["lockpickSkill"]["trainitem"] = False
        #user items
        users[str(user.id)]["items"] = {}
        users[str(user.id)]["items"]["weed"] = 0
        users[str(user.id)]["items"]["lockpick"] = 1
    #dumping dose variables   
    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return

def get_bank_data():
    try:
        with open("mainbank.json","r") as f:
            users = json.load(f)
        return users
    except FileNotFoundError:
        f = open("mainbank.json", "w")
        f.write("{")
        f.write("}")
        f.close
        with open("mainbank.json","r") as f:
            users = json.load(f)
        return users

def update_bank(user,change = 0):
    open_account(user)
    users = get_bank_data()

    users[str(user.id)]["bal"] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return

async def lvlup(ctx, user, xp):
    open_account(user)
    users = get_bank_data()
    userdata = users[str(user.id)]

    userdata["lvlprogress"] += xp

    while userdata["lvlprogress"] >= 100 * (userdata["lvl"]**1.5):
        userdata["lvlprogress"] -= 100 * (userdata["lvl"]**1.5)
        userdata["lvl"] += 1
        userdata_lvl = userdata["lvl"]

        em = discord.Embed(title = f"LVL UP!", description = f"{ctx.author.name} is nu lvl `{userdata_lvl}`!", color = discord.Color.blue())

        await ctx.send(embed = em)
          
    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return

async def skill_lvlup(ctx, user, skill, xp):
    open_account(user)
    users = get_bank_data()

    user_skill = users[str(user.id)]["Skills"][skill]

    user_skill["lvlprogress"] += xp

    user_skill_lvl = user_skill["lvl"]

    while user_skill["lvlprogress"] >= 100 * (user_skill_lvl**1.5):
        user_skill["lvlprogress"] -= 100 * (user_skill_lvl**1.5)
        user_skill["lvl"] += 1
        user_skill_lvl = user_skill["lvl"]

        em = discord.Embed(title = f"SKILL LVL UP", description = f"{ctx.author.name}'s {skill} is nu lvl `{user_skill_lvl}`!", color = discord.Color.blue())

        await ctx.send(embed = em)
    
    user_skill["boost"] = 5*int(user_skill["lvl"])

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return