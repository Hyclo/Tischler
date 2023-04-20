import discord
import distributioner
import datetime
import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def get_difference_in_hours(date_1):
    date_format_str = "%Y-%m-%d %H:%M"

    now = datetime.datetime.now()
        
    now = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M")
    
    start = datetime.datetime.strptime(date_1, date_format_str)
    end =   datetime.datetime.strptime(now, date_format_str)
    # Get interval between two timstamps as timedelta object
    diff = end - start
    # Get interval between two timstamps in hours
    diff_in_hours = diff.total_seconds() / 3600
    
    return diff_in_hours

async def check_time(ctx):
    if get_difference_in_hours(distributioner.get(ctx.author.id, "timestampwork")) < 24:
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
    if await distributioner.check_user(ctx) == False:
        return
    
    if await check_time(ctx) == False:
        return
    
    if distributioner.get(ctx.author.id, "working") == "True":
        embed = discord.Embed(
            title="406 Not Acceptable",
            description= "Just kidding " + ctx.author.mention + " but u are already working!",
            color=discord.Colour.dark_red()
        )
        await ctx.respond(embed=embed)
    else:
        
        now = datetime.datetime.now()
        
        now = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M")
        
        distributioner.update(ctx.author.id, "working", str(True))
        distributioner.update(ctx.author.id, "timestampwork", now)
        
        embed = discord.Embed(
            title="Tischler",
            description=ctx.author.mention + " started working!",
            color=discord.Colour.blurple()
        )
        await ctx.respond(embed=embed)
    

async def end_working(ctx):
    
    if await distributioner.check_user(ctx) == False:
        return
    
    if distributioner.get(ctx.author.id, "working") == "False":
        embed = discord.Embed(
            title="406 Not Acceptable",
            description= "Just kidding " + ctx.author.mention + " but u have to work first to get paid!",
            color=discord.Colour.dark_red()
        )
        await ctx.respond(embed=embed)
    else:
        
        money = 10 * (distributioner.get(ctx.author.id, "level") + 1) * get_difference_in_hours(distributioner.get(ctx.author.id, "timestampwork"))
        
        money = round_up(money)
        
        embed = discord.Embed(
            title="Tischler",
            description=ctx.author.mention + " you are done with work for now working!",
            color=discord.Colour.blurple()
        )
        embed.add_field(name="Money made", value=str(money), inline=True)

        now = datetime.datetime.now()
        
        now = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M")
        
        distributioner.update(ctx.author.id, "timestampwork", now)
        
        distributioner.update(ctx.author.id, "working", str(False))
        
        distributioner.add(ctx.author.id, "money", money)
        
        await ctx.respond(embed=embed)
        
        return


