from discord.ext import commands
import discord
from discord.utils import get
import json
import os
import random

bot = commands.Bot(command_prefix=";", intents=discord.Intents.all())

bot.remove_command('help')

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing,name=f"Buy @ discord.gg/maplepredictor"))
  print(f"maple ")

@bot.command()
@commands.has_role("Owner")
async def whitelist(ctx, member : discord.Member):
    await ctx.message.delete()
    role = get(member.guild.roles, name="Customer")
    await member.add_roles(role)
    em = discord.Embed(description=f"<a:success:1015040067720466432> `Whitelisted` {member.mention}", color=0x2f3136)
    await ctx.send(embed=em)

@bot.command()
@commands.has_role("Owner")
async def dewhitelist(ctx, member : discord.Member):
    await ctx.message.delete()
    role = get(member.guild.roles, name="Customer")
    await member.remove_roles(role)
    em = discord.Embed(description=f"<a:success:1015040067720466432> `Unwhitelisted` {member.mention}", color=0x2f3136)
    await ctx.send(embed=em)

@bot.command()
@commands.has_role("Customer")
async def crash(ctx):
    prediction = round(random.uniform(1, 11), 2)
    em = discord.Embed(color=0x2f3136)
    em.add_field(name="<a:crash:1014956565293441045> Crash Prediction", value=(f"```⇀ {prediction}x```"))
    em.set_footer(text="Note: NOT all predictions will be a 100% accurate.", icon_url="https://media.discordapp.net/attachments/1014588018335699065/1014931096959463484/unknown.png")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/1014588018335699065/1014931096959463484/unknown.png")
    await ctx.author.send(embed=em)


@bot.command()
@commands.has_role("Customer")
async def mines(ctx, round_id):
  round_id = str(round_id)
  round_length = len(round_id)

  if round_length < 36:
    em = discord.Embed(description="<:ex:1015040061546442853> Invalid Round `ID`", color=0x2f3136)
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
    description="\n" + "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + "\n" + "**Probability**" + "\n" + f"```⇀ {info}%```", color=0x2f3136)
    em.set_footer(text="Note: NOT all predictions will be a 100% accurate.", icon_url="https://media.discordapp.net/attachments/1014588018335699065/1014931096959463484/unknown.png")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/1014588018335699065/1014931096959463484/unknown.png")
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
    em = discord.Embed(description="\n__**Crash**__\n```⇀ Predicts when the game would possibly crash.\nUse ;crash```\n__**Mines**__\n```⇀ Predicts the possible outcome of the next game of mines.\nUse ;mines```",color=0x2f3136)
    em.set_author(icon_url="https://media.discordapp.net/attachments/1014588018335699065/1014931096959463484/unknown.png", name="Maple")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/1014588018335699065/1014931096959463484/unknown.png")
    em.set_footer(text=f"Note: NOT all predictions will be a 100% accurate.", icon_url="https://media.discordapp.net/attachments/1014588018335699065/1014931096959463484/unknown.png")
    await ctx.author.send(embed=em)

bot.run(os.environ["DISCORD_TOKEN"])
