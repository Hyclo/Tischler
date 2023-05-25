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
from gamling.dice import dice
from gamling.online_dice import send_request
from migration_db.migrate import migrate
from work.work import start_working
from work.work import end_working
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

@tasks.loop(hours=24.0)
async def reset_online_gambling():
    with open('gamling/online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        while len(requests) >= 0:
            print(requests)
            requests.pop()

        tmp_request = {
            "requestee": "I_have_requested_a_battle",
            "requested": "I_have_been_requested_to_battle",
            "betting_amount": 1000
        }

        requests.append(tmp_request)

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
async def slash_dice(ctx, amount: Option(int, "gamble money", required=True, default='')):
    await dice(ctx, amount, bot)
    
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

@bot.slash_command(name = "challenge", description = "challenge an other user to a game of dice")
async def slashsend_request(ctx, member: Option(discord.Member, " your friends name", required=True, default='null'),
            bet: Option(int, " how much you want to bet", required=True, default='null')):
    await send_request(ctx, member, bet)
    
@bot.slash_command(name = "redeploy", description = "redeploy bot, only for developers")
async def slash_redeploy(ctx):
    if pentester.check_lenillian(ctx) == False:
        return
    else:
        await ctx.respond("Starting new deployment, I'm up again in 20s")
        subprocess.call(['bash', './deployment/auto-deploy.sh'])

reset_online_gambling.start()
backup.start()
bot.run(os.getenv('TOKEN'))
