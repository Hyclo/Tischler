import discord
from discord.commands import Option
import os
from dotenv import load_dotenv
import datetime
from discord.ext import tasks
import subprocess
import pentester
import json

# file imports start
from user.login import login
from user.profile import profile
from user.leaderboard import leaderboard
from user.level import level
from user.level import rank
from money.balance import balance
from money.daily import daily
from money.forbes import forbes
from money.send_money import send_money
from gamling.online_dice import dice_chooser
from gamling.online_dice import accept
from gamling.online_dice import deny
from gamling.online_dice import clear_requests
from migration_db.migrate import migrate
from work.work import start_working
from work.work import end_working
from stocks.hourly_job import stocks_job
# file imports end

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
    
    await level(message.author.id, message, bot)

@tasks.loop(hours=1.0)
async def backup():
    subprocess.call(['bash', './backup/backup.sh'])

@tasks.loop(seconds=1.0)
async def stocks():
    await stocks_job(bot)

@tasks.loop(hours=24.0)
async def reset_online_gambling():
    with open('gamling/online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        while len(requests) > 1:

            requests.pop()

    with open("gamling/online_dice.json", "w") as outfile:
        json.dump(data, outfile)

# commands

@bot.slash_command(name = "latency", description = "check the latency of Schreiner")
async def check_latency(ctx):
    await ctx.respond("I'll respond in "+str(bot.latency)+"s")

@bot.slash_command(name = "login", description = "login as tischler")
async def slash_login(ctx):
    await login(ctx, bot)
    
@bot.slash_command(name = "profile", description = "see your tischler working id")
async def slash_profile(ctx, member: Option(discord.Member, "an other user", required=False, default='null')):
    await profile(ctx, bot, member)

@bot.slash_command(name = "balance", description = "see how much money you have")
async def slash_balance(ctx):
    await balance(ctx)
    
@bot.slash_command(name = "daily", description = "get your daily salary to feed your family")
async def slash_daily(ctx):
    await daily(ctx)
    
@bot.slash_command(name = "forbes", description = "see the three richest tischlers")
async def slash_forbes(ctx):
    await forbes(ctx, bot)
    
@bot.slash_command(name = "leaderboard", description = "see the three top ranked tischlers")
async def slash_leaderboard(ctx):
    await leaderboard(ctx, bot)
    
@bot.slash_command(name = "dice", description = "throw the dice better than me to win some money")
async def slash_dice(ctx, value: Option(int, "gamble money", required=True, default=''), 
            member: Option(discord.Member, " your friends name", required=False, default='none')):
    await dice_chooser(ctx, value, member, bot)
    
@bot.slash_command(name = "migrate", description = "add new db item")
async def slash_migrate(ctx, key: Option(str, "new key", required=True, default=''),
            value: Option(str, "default value", required=True, default='')):
    await migrate(ctx, key, value)
    
@bot.slash_command(name = "work", description = "work to get more money")
async def slash_work(ctx):
    await start_working(ctx)
    
@bot.slash_command(name = "payday", description = "get your payday")
async def slash_payday(ctx):
    await end_working(ctx)
    
@bot.slash_command(name = "transfer", description = "transfer money to a friend")
async def slash_send_money(ctx, member: Option(discord.Member, " your friends name", required=True, default=''),
            value: Option(int, " how much money you wanna send", required=True, default='')):
    await send_money(ctx, value, member, bot)

@bot.slash_command(name = "rank", description = "the rank of you or the given user")
async def slash_rank(ctx, member: Option(discord.Member, " your friends name", required=False, default='null')):
    await rank(ctx, member, bot)

@bot.slash_command(name = "challenge_accept", description = "accept the challenge of an other user to a game of dice")
async def slash_accept(ctx, member: Option(discord.Member, " your friends name", required=True, default='null')):
    await accept(ctx, member)

@bot.slash_command(name = "challenge_deny", description = "deny the challenge an other user to a game of dice")
async def slash_deny(ctx, member: Option(discord.Member, " your friends name", required=True, default='null')):
    await deny(ctx, member)

@bot.slash_command(name = "challenge_clear", description = "clear your requests")
async def slash_clear_requests(ctx):
    await clear_requests(ctx)

stocks.start()
reset_online_gambling.start()
backup.start()
bot.run(os.getenv('TOKEN'))
