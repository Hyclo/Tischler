import discord
import distrib
import datetime
import math
import pentester

def round_up(n, decimals):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def get_difference_in_hours(date_1):
    date_format_str = "%Y-%m-%d %H:%M"

    now = datetime.datetime.now()
        
    now = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M")
    
    start = datetime.datetime.strptime(date_1, date_format_str)
    end =   datetime.datetime.strptime(now, date_format_str)
    # Get interval between two timestamps as timedelta object
    diff = end - start
    # Get interval between two timestamps in hours
    diff_in_hours = diff.total_seconds() / 3600
    
    return diff_in_hours

async def check_time(ctx):
    if get_difference_in_hours(distrib.get_user(ctx.author.id).timestampwork) < 24:
        embed = discord.Embed(
            title="406 Not Acceptable",
            description= "Just kidding " + ctx.author.mention + " but you have to take a 24 hour break",
            color=discord.Colour.dark_red()
        )
        await ctx.respond(embed=embed)
        return False
    else:
        return True
    

async def start_working(ctx):
    if await pentester.check_user(ctx, ctx.author) == False:
        return
    
    if await check_time(ctx) == False:
        return
    
    if distrib.get_user(ctx.author.id).working == "True":
        embed = discord.Embed(
            title="406 Not Acceptable",
            description= "Just kidding " + ctx.author.mention + " but u are already working!",
            color=discord.Colour.dark_red()
        )
        await ctx.respond(embed=embed)
    else:
        
        now = datetime.datetime.now()
        
        now = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M")
        
        distrib.update(ctx.author.id, "working", str(True))
        distrib.update(ctx.author.id, "timestampwork", now)
        
        embed = discord.Embed(
            title="Tischler",
            description=ctx.author.mention + " started working!",
            color=discord.Colour.blurple()
        )
        await ctx.respond(embed=embed)
    

async def end_working(ctx):
    
    if await pentester.check_user(ctx, ctx.author) == False:
        return
    
    if distrib.get_user(ctx.author.id).working == "False":
        embed = discord.Embed(
            title="406 Not Acceptable",
            description= "Just kidding " + ctx.author.mention + " but u have to work first to get paid!",
            color=discord.Colour.dark_red()
        )
        await ctx.respond(embed=embed)
    else:
        worked_hours = round_up(get_difference_in_hours(distrib.get_user(ctx.author.id).timestampwork), 2)

        money = worked_hours * 10 * ((distrib.get_user(ctx.author.id).level + 1) / 10)
        
        money = round_up(money, 0)
        
        embed = discord.Embed(
            title="Tischler",
            description=ctx.author.mention + " you are done with work for now working!",
            color=discord.Colour.blurple()
        )
        embed.add_field(name="Money made", value=str(money), inline=True)

        now = datetime.datetime.now()
        
        now = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M")
        
        distrib.update(ctx.author.id, "timestampwork", now)
        
        distrib.update(ctx.author.id, "working", str(False))
        
        distrib.add_up_value(ctx.author.id, "money", money)

        embed.add_field(name="Hours worked", value=str(worked_hours) + "h", inline=True)
        
        await ctx.respond(embed=embed)
        
        return


