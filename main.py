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

@bot.command()
@commands.has_role("customer")
async def crash(ctx):
    prediction = round(random.uniform(1, 4), 2)
    
    if prediction > 3.0:
      em = discord.Embed(title="__**Crash Prediction**__", color=0x2f3136)
      em.add_field(name="**Probably Above**", value=(f"```⇀ 3.0x — Most likely to crash at {prediction}x```"))
      em.set_footer(text="Note: NOT all predictions will be a 100% accurate.", icon_url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg")
      em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg")
      await ctx.author.send(embed=em)
      
    else:
      em = discord.Embed(title="__**Crash Prediction**__", color=0x2f3136)
      em.add_field(name="**Around**", value=(f"```⇀ {prediction}x```"))
      em.set_footer(text="Note: NOT all predictions will be a 100% accurate.", icon_url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg")
      em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg")
      await ctx.author.send(embed=em)
      

@bot.command()
@commands.has_role("customer")
async def towers(ctx, round_id):
  round_id = str(round_id)
  round_length = len(round_id)
  
  if round_length < 36:
    em = discord.Embed(description="<:error:995036612897554442> Invalid Round ID", color=0x2f3136)
    await ctx.author.send(embed=em)
    
  elif round_length == 36:
    tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24,tower25 = "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>"
    
    a = random.randint(1, 3)
    b = random.randint(1, 3)
    c = random.randint(1, 3)
    d = random.randint(1, 3)
    e = random.randint(1, 3)
    f = random.randint(1, 3)
    g = random.randint(1, 3)
    h = random.randint(1, 3)

    if a == 1:
      tower1 = "<:6648staricon:1026243646758076426>"
    elif a == 2:
      tower2 = "<:6648staricon:1026243646758076426>"
    elif a == 3:
      tower3 = "<:6648staricon:1026243646758076426>"

    if b == 1:
      tower4 = "<:6648staricon:1026243646758076426>"
    elif b == 2:
      tower5 = "<:6648staricon:1026243646758076426>"
    elif b == 3:
      tower6 = "<:6648staricon:1026243646758076426>"

    if c == 1:
      tower7 = "<:6648staricon:1026243646758076426>"
    elif c == 2:
      tower8 = "<:6648staricon:1026243646758076426>"
    elif c == 3:
      tower9 = "<:6648staricon:1026243646758076426>"

    if d == 1:
      tower10 = "<:6648staricon:1026243646758076426>"
    elif d == 2:
      tower11 = "<:6648staricon:1026243646758076426>"
    elif d == 3:
      tower12 = "<:6648staricon:1026243646758076426>"

    if e == 1:
      tower13 = "<:6648staricon:1026243646758076426>"
    elif e == 2:
      tower14 = "<:6648staricon:1026243646758076426>"
    elif e == 3:
      tower15 = "<:6648staricon:1026243646758076426>"

    if f == 1:
      tower16 = "<:6648staricon:1026243646758076426>"
    elif f == 2:
      tower17 = "<:6648staricon:1026243646758076426>"
    elif f == 3:
      tower18 = "<:6648staricon:1026243646758076426>"

    if g == 1:
      tower19 = "<:6648staricon:1026243646758076426>"
    elif g == 2:
      tower20 = "<:6648staricon:1026243646758076426>"
    elif g == 3:
      tower21 = "<:6648staricon:1026243646758076426>"

    if h == 1:
      tower22 = "<:6648staricon:1026243646758076426>"
    elif h == 2:
      tower23 = "<:6648staricon:1026243646758076426>"
    elif h == 3:
      tower24 = "<:6648staricon:1026243646758076426>"


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
    em.set_footer(text="Note: NOT all predictions will be a 100% accurate.", icon_url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg")
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg")
    await ctx.author.send(embed=em)

    
@bot.command()
@commands.has_role("customer")
async def mines(ctx, round_id):
  round_id = str(round_id)
  round_length = len(round_id)

  if round_length < 36:
    em = discord.Embed(description="<:error:995036612897554442> **Invalid** `Round ID`", color=0x2f3136)
    await ctx.author.send(embed=em)

  elif round_length  == 36:
    mine1,mine2,mine3,mine4,mine5,mine6,mine7,mine8,mine9,mine10,mine11,mine12,mine13,mine14,mine15,mine16,mine17,mine18,mine19,mine20,mine21,mine22,mine23,mine24,mine25 = "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>", "<:error:995036612897554442>"

    a = random.randint(1, 8)
    b = random.randint(9, 13)
    c = random.randint(14, 17)
    d = random.randint(18, 25)

    if a == 1:
      mine1 ="<a:9887greentick:1026243969094533223>"
    elif a == 2:
      mine2 ="<a:9887greentick:1026243969094533223>"
    elif a == 3:
      mine3 ="<a:9887greentick:1026243969094533223>"
    elif a == 4:
      mine4 ="<a:9887greentick:1026243969094533223>"
    elif a == 5:
      mine5 ="<a:9887greentick:1026243969094533223>"
    elif a == 6:
      mine6 ="<a:9887greentick:1026243969094533223>"
    elif a == 7:
      mine7 ="<a:9887greentick:1026243969094533223>"
    elif a == 8:
      mine8 ="<a:9887greentick:1026243969094533223>"

    if b == 9:
      mine9 ="<a:9887greentick:1026243969094533223>"
    elif b == 10:
      mine10 ="<a:9887greentick:1026243969094533223>"
    elif b == 11:
      mine11 ="<a:9887greentick:1026243969094533223>"
    elif b == 12:
      mine12 ="<a:9887greentick:1026243969094533223>"
    elif b == 13:
      mine13 ="<a:9887greentick:1026243969094533223>"

    if c == 14:
      mine14 ="<a:9887greentick:1026243969094533223>"
    elif c == 15:
      mine15 ="<a:9887greentick:1026243969094533223>"
    elif c == 16:
      mine16 ="<a:9887greentick:1026243969094533223>"
    elif c == 17:
      mine17 ="<a:9887greentick:1026243969094533223>"
    
    if d == 18:
      mine18 ="<a:9887greentick:1026243969094533223>"
    elif d == 19:
      mine19 ="<a:9887greentick:1026243969094533223>"
    elif d == 20:
      mine20 ="<a:9887greentick:1026243969094533223>"
    elif d == 21:
      mine21 ="<a:9887greentick:1026243969094533223>"
    elif d == 22:
      mine22 ="<a:9887greentick:1026243969094533223>"
    elif d == 23:
      mine23 ="<a:9887greentick:1026243969094533223>"
    elif d == 24:
      mine24 ="<a:9887greentick:1026243969094533223>"
    elif d == 25:
      mine25 ="<a:9887greentick:1026243969094533223>"

    row1 = mine1 + mine2 + mine3 + mine4 + mine5 
    row2 = mine6 + mine7 + mine8 + mine9 + mine10
    row3 = mine11 + mine12 + mine13 + mine14 + mine15
    row4 = mine16 + mine17 + mine18 + mine19 + mine20
    row5 = mine21 + mine22 + mine23 + mine24 + mine25
    
    info = str(random.randint(75, 92))

    em = discord.Embed(title="Lotus Prediction",
    description="\n" + "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + "\n" + "**Accuracy**" + "\n" + f"```⇀ {info}%```", color=0x2f3136)
    em.set_footer(text="Note: NOT all predictions will be a 100% accurate.", icon_url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg")
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg")
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
    em = discord.Embed(description="\n__**Crash**__\n```⇀ Predicts when the game would possibly crash.\nUse ;crash```\n__**Mines**__\n```⇀ Predicts the possible outcome of the next game of mines.\nUse ;mines [round id]\n```__**Towers**__\n```⇀ Predicts the possible outcome of the next game of towers.\nUse ;towers [round id]```",color=0x2f3136)
    em.set_author(icon_url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg", name="Lotus")
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg")
    em.set_footer(text=f"Note: NOT all predictions will be a 100% accurate.", icon_url="https://cdn.discordapp.com/attachments/1025741459976106094/1026242675780894730/9b0743b77a8857bf7233205c936d0d6c.jpg")
    await ctx.author.send(embed=em)

bot.run('MTAyNjIzOTEwNTg0NTE4MjQ2NQ.GWHXgx.JXFbqw58T3XGetPqh_YLMKgGQNQZlPq4HpPb7c')
