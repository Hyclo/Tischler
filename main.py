import discord
from discord.commands import Option
import os
from dotenv import load_dotenv
import datetime
from discord.ext import tasks
import subprocess

# file imports start
from user.login import login
from user.profile import profile
from money.balance import balance
from money.daily import daily
from money.forbes import forbes
from money.send_money import send_money
from gamling.dice import dice
from migration_db.migrate import migrate
from work.work import start_working
from work.work import end_working
from user.level import level
from deployment.deployment import deployment
# file imports end

deployee = deployment()

load_dotenv() # load all the variables from the env file
bot = discord.AutoShardedBot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    print("time of login: " + str(datetime.datetime.today()))
    
@bot.event
async def on_message(message):
    if message.author.id == 1096041999011950632:
        return
    
    await level(message.author.id)

@tasks.loop(hours=24.0)
async def deploy():
    if deployee.get_stopper() == 0:
        bot.get_guild(908337305759141948).get_channel(978033714573488169).send("Starting new deployment")
        subprocess.call(['bash', './deployment/auto-deploy.sh'])
        bot.get_guild(908337305759141948).get_channel(978033714573488169).send("switched old with new deployment")

    if deployee.get_stopper() == 1:
        deployee.set_stopper(0)

@bot.slash_command(name = "latency", description = "check the latency of Schreiner")
async def check_latency(ctx):
    await ctx.respond("I'll respond in "+str(bot.latency)+"s")

@bot.slash_command(name = "login", description = "login as tischler")
async def slash_login(ctx):
    await login(ctx, bot)
    
@bot.slash_command(name = "profile", description = "see your tischler working id")
async def slash_profile(ctx):
    await profile(ctx, bot)

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
    
@bot.slash_command(name = "migrate", description = "add new db item")
async def slash_migrate(ctx, key: Option(str, "new key", required=True, default=''), value: Option(str, "default value", required=True, default='')):
    await migrate(ctx, key, value)
    
@bot.slash_command(name = "work", description = "work to get more money")
async def slash_work(ctx):
    await start_working(ctx)
    
@bot.slash_command(name = "payday", description = "get your payday")
async def slash_payday(ctx):
    await end_working(ctx)
    
@bot.slash_command(name = "transfer", description = "transfer money to a friend")
async def slash_send_money(ctx, member: Option(discord.Member, " your friends name", required=True, default=''), value: Option(int, " how much money you wanna send", required=True, default='')):
    await send_money(ctx, value, member)


deploy.start()
bot.run(os.getenv('TOKEN'))