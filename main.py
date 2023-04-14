import discord
from discord.ext import tasks
from discord.commands import Option
from discord.commands.context import ApplicationContext
import os
from dotenv import load_dotenv
import datetime

# file imports start
from user.login import login
from money.balance import balance
from money.daily import daily
from money.forbes import forbes
from gamling.dice import dice
# file imports end

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    print("time of login: " + str(datetime.datetime.today()))

@bot.slash_command(name = "latency", description = "check the latency of Schreiner")
async def check_latency(ctx):
    await ctx.respond("I'll respond in "+str(bot.latency)+"s")

@bot.slash_command(name = "login", description = "login as tischler")
async def slash_login(ctx):
    await login(ctx)

@bot.slash_command(name = "balance", description = "see how much money you have")
async def slash_balance(ctx):
    await balance(ctx)
    
@bot.slash_command(name = "daily", description = "get your daily salary to feed your family")
async def slash_daily(ctx):
    await daily(ctx)
    
@bot.slash_command(name = "forbes", description = "see the three richest tischlers")
async def slash_forbes(ctx):
    await forbes(ctx, bot)
    
@bot.slash_command(name = "dice", description = "throw the dice better than me to win some money")
async def slash_dice(ctx, amount: Option(int, "gamble money", required=True, default='')):
    await dice(ctx, amount)
    

bot.run(os.getenv('TOKEN'))