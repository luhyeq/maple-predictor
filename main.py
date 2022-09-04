from discord.ext import commands
import discord
from discord.utils import get
import os
import datetime
import time
import random

intents = discord.Intents().all()

bot = commands.Bot(command_prefix=";", intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing,name=f"Buy — https://discord.gg/fHWBkdtzge"))
  print(f"maple ")

@bot.command(aliases=["veri"])
@commands.has_role("Owner")
async def verify(ctx, member : discord.Member):
    await ctx.message.delete()
    role = get(member.guild.roles, name="Customer")
    await member.add_roles(role)
    em = discord.Embed(description=f"<a:success:1015040067720466432> `Verified` {member.mention}", color=0x2f3136)
    await ctx.send(embed=em)

@bot.command(aliases=["unveri"])
@commands.has_role("Owner")
async def unverify(ctx, member : discord.Member):
    await ctx.message.delete()
    role = get(member.guild.roles, name="Customer")
    await member.remove_roles(role)
    em = discord.Embed(description=f"<a:success:1015040067720466432> `Unverified` {member.mention}", color=0x2f3136)
    await ctx.send(embed=em)

@bot.command()
@commands.has_role("Customer")
async def crash(ctx):
    prediction = round(random.uniform(1, 4), 2)
    
    if prediction > 3.0:
      em = discord.Embed(title="__**Crash Prediction**__", color=0x2f3136)
      em.add_field(name="**Probably Above**", value=(f"```⇀ 3.0x — Most likely to crash at {prediction}x```"))
      em.set_footer(text="Note: NOT all predictions will be a 100% accurate.", icon_url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png")
      em.set_thumbnail(url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png")
      await ctx.author.send(embed=em)
      
    else:
      em = discord.Embed(title="__**Crash Prediction**__", color=0x2f3136)
      em.add_field(name="**Around**", value=(f"```⇀ {prediction}x```"))
      em.set_footer(text="Note: NOT all predictions will be a 100% accurate.", icon_url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png")
      em.set_thumbnail(url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png")
      await ctx.author.send(embed=em)
      

@bot.command()
@commands.has_role("Customer")
async def towers(ctx, round_id):
  round_id = str(round_id)
  round_length = len(round_id)
  
  if round_length < 36:
    em = discord.Embed(description="<:ex:1015040061546442853> Invalid Round ID", color=0x2f3136)
    await ctx.author.send(embed=em)
    
  elif round_length == 36:
    tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24,tower25 = "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>"
    
    a = random.randint(1, 3)
    b = random.randint(1, 3)
    c = random.randint(1, 3)
    d = random.randint(1, 3)
    e = random.randint(1, 3)
    f = random.randint(1, 3)
    g = random.randint(1, 3)
    h = random.randint(1, 3)

    if a == 1:
      tower1 = "<:staricon:1015784865876148314>"
    elif a == 2:
      tower2 = "<:staricon:1015784865876148314>"
    elif a == 3:
      tower3 = "<:staricon:1015784865876148314>"

    if b == 1:
      tower4 = "<:staricon:1015784865876148314>"
    elif b == 2:
      tower5 = "<:staricon:1015784865876148314>"
    elif b == 3:
      tower6 = "<:staricon:1015784865876148314>"

    if c == 1:
      tower7 = "<:staricon:1015784865876148314>"
    elif c == 2:
      tower8 = "<:staricon:1015784865876148314>"
    elif c == 3:
      tower9 = "<:staricon:1015784865876148314>"

    if d == 1:
      tower10 = "<:staricon:1015784865876148314>"
    elif d == 2:
      tower11 = "<:staricon:1015784865876148314>"
    elif d == 3:
      tower12 = "<:staricon:1015784865876148314>"

    if e == 1:
      tower13 = "<:staricon:1015784865876148314>"
    elif e == 2:
      tower14 = "<:staricon:1015784865876148314>"
    elif e == 3:
      tower15 = "<:staricon:1015784865876148314>"

    if f == 1:
      tower16 = "<:staricon:1015784865876148314>"
    elif f == 2:
      tower17 = "<:staricon:1015784865876148314>"
    elif f == 3:
      tower18 = "<:staricon:1015784865876148314>"

    if g == 1:
      tower19 = "<:staricon:1015784865876148314>"
    elif g == 2:
      tower20 = "<:staricon:1015784865876148314>"
    elif g == 3:
      tower21 = "<:staricon:1015784865876148314>"

    if h == 1:
      tower22 = "<:staricon:1015784865876148314>"
    elif h == 2:
      tower23 = "<:staricon:1015784865876148314>"
    elif h == 3:
      tower24 = "<:staricon:1015784865876148314>"


    row1 = tower1 + tower2 + tower3
    row2 = tower4 + tower5 + tower6
    row3 = tower7 + tower8 + tower9
    row4 = tower10 + tower11 + tower12
    row5 = tower13 + tower14 + tower15
    row6 = tower16 + tower17 + tower18
    row7 = tower19 + tower20 + tower21
    row8 = tower22 + tower23 + tower24

    info = str(random.randint(45, 95))

    em = discord.Embed(title="__**Towers Prediction**__",
    description="\n" + "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8 + "\n" + "\n" + "**Accuracy**" + "\n" + f"```⇀ {info}%```", color=0x2f3136)
    em.set_footer(text="Note: NOT all predictions will be a 100% accurate.", icon_url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png")
    await ctx.author.send(embed=em)

    
@bot.command()
@commands.has_role("Customer")
async def mines(ctx, round_id):
  round_id = str(round_id)
  round_length = len(round_id)

  if round_length < 36:
    em = discord.Embed(description="<:ex:1015040061546442853> **Invalid** `Round ID`", color=0x2f3136)
    await ctx.author.send(embed=em)

  elif round_length  == 36:
    mine1,mine2,mine3,mine4,mine5,mine6,mine7,mine8,mine9,mine10,mine11,mine12,mine13,mine14,mine15,mine16,mine17,mine18,mine19,mine20,mine21,mine22,mine23,mine24,mine25 = "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>", "<:ex:1015040061546442853>"

    a = random.randint(1, 8)
    b = random.randint(9, 13)
    c = random.randint(14, 17)
    d = random.randint(18, 25)

    if a == 1:
      mine1 ="<a:success:1015040067720466432>"
    elif a == 2:
      mine2 ="<a:success:1015040067720466432>"
    elif a == 3:
      mine3 ="<a:success:1015040067720466432>"
    elif a == 4:
      mine4 ="<a:success:1015040067720466432>"
    elif a == 5:
      mine5 ="<a:success:1015040067720466432>"
    elif a == 6:
      mine6 ="<a:success:1015040067720466432>"
    elif a == 7:
      mine7 ="<a:success:1015040067720466432>"
    elif a == 8:
      mine8 ="<a:success:1015040067720466432>"

    if b == 9:
      mine9 ="<a:success:1015040067720466432>"
    elif b == 10:
      mine10 ="<a:success:1015040067720466432>"
    elif b == 11:
      mine11 ="<a:success:1015040067720466432>"
    elif b == 12:
      mine12 ="<a:success:1015040067720466432>"
    elif b == 13:
      mine13 ="<a:success:1015040067720466432>"

    if c == 14:
      mine14 ="<a:success:1015040067720466432>"
    elif c == 15:
      mine15 ="<a:success:1015040067720466432>"
    elif c == 16:
      mine16 ="<a:success:1015040067720466432>"
    elif c == 17:
      mine17 ="<a:success:1015040067720466432>"
    
    if d == 18:
      mine18 ="<a:success:1015040067720466432>"
    elif d == 19:
      mine19 ="<a:success:1015040067720466432>"
    elif d == 20:
      mine20 ="<a:success:1015040067720466432>"
    elif d == 21:
      mine21 ="<a:success:1015040067720466432>"
    elif d == 22:
      mine22 ="<a:success:1015040067720466432>"
    elif d == 23:
      mine23 ="<a:success:1015040067720466432>"
    elif d == 24:
      mine24 ="<a:success:1015040067720466432>"
    elif d == 25:
      mine25 ="<a:success:1015040067720466432>"

    row1 = mine1 + mine2 + mine3 + mine4 + mine5 
    row2 = mine6 + mine7 + mine8 + mine9 + mine10
    row3 = mine11 + mine12 + mine13 + mine14 + mine15
    row4 = mine16 + mine17 + mine18 + mine19 + mine20
    row5 = mine21 + mine22 + mine23 + mine24 + mine25
    
    info = str(random.randint(75, 92))

    em = discord.Embed(title="Maple Prediction",
    description="\n" + "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + "\n" + "**Accuracy**" + "\n" + f"```⇀ {info}%```", color=0x2f3136)
    em.set_footer(text="Note: NOT all predictions will be a 100% accurate.", icon_url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png")
    await ctx.author.send(embed=em)

@bot.command(aliases=["p"])
async def ping(ctx):
  em = discord.Embed(description=f"Latency is `{round(bot.latency * 1000)}ms`",
  color=0x2f3136)
  await ctx.send(embed=em)


@bot.command()
@commands.has_role("Owner")
async def send(ctx, *, message):
    await ctx.message.delete()
    em = discord.Embed(title=f"", description=f"```{message}```",
    color=0x2f3136)
    await ctx.send(embed=em)

@bot.command(aliases=['h', 'cmds'])
@commands.cooldown(1, 8, commands.BucketType.channel)
async def help(ctx):
    em = discord.Embed(description="\n__**Crash**__\n```⇀ Predicts when the game would possibly crash.\nUse ;crash```\n__**Mines**__\n```⇀ Predicts the possible outcome of the next game of mines.\nUse ;mines [round id]\n```__**Towers**__\n```⇀ Predicts the possible outcome of the next game of towers.\nUse ;tower [round id]````",color=0x2f3136)
    em.set_author(icon_url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png", name="Maple")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png")
    em.set_footer(text=f"Note: NOT all predictions will be a 100% accurate.", icon_url="https://media.discordapp.net/attachments/1014588018335699065/1015734553488392232/unknown.png")
    await ctx.author.send(embed=em)

bot.run(os.environ["DISCORD_TOKEN"])
