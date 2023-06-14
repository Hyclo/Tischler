import pentester
import distrib
import datetime
import random
import discord
import math
import fotographer
import asyncio

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
    diff_in_minutes = diff.total_seconds() / 60
    
    return diff_in_minutes

async def level(author_id, message, bot):
    
    if await pentester.is_user_in_db(author_id) == False:
        return
    
    if get_difference_in_hours(distrib.get_user(author_id).timestamplevel) < 1:
        return
    else:
        distrib.update(author_id, "timestamplevel" ,datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M"))
        
        distrib.add_up_value(author_id, "exp", random.randint(15,25))
        
        user = distrib.get_user(author_id)
        
        result = 0
        stolen_levels = user.level
        while stolen_levels >= 0:
            result += 5 * ((level-stolen_levels) ** 2) + ((level-stolen_levels) * 50) + 100
            stolen_levels = stolen_levels - 1
        
        if user.exp >= result:
            
            distrib.add_up_value(author_id, "level", 1)
            
            embed = discord.Embed(
                title="Level up",
                description= "<@" + str(message.author.id) + "> you have reached a new level!",
                color=discord.Colour.blurple()
            )
            embed.add_field(name="current Level " + str(level + 1), value="", inline=True)
            await message.reply(embed=embed)


async def rank(ctx, member, bot):

    message = await ctx.respond(ctx.author.mention + " your level is being calculated...")
    
    ctx_author = ctx.author

    if member != 'null':
        ctx_author = await bot.get_or_fetch_user(member.id)
    
    if await pentester.check_user(ctx, ctx_author) == False:
        return

    user = distrib.get_user(ctx_author.id)

    stolen_levels = user.level

    required_exp = 0
    while stolen_levels >= 0:
        required_exp += 5 * ((user.level-stolen_levels) ** 2) + ((user.level-stolen_levels) * 50) + 100
        stolen_levels = stolen_levels - 1

    current_level_required_exp = 0
    while (stolen_levels - 1)>= 0:
        current_level_required_exp += 5 * ((level-stolen_levels) ** 2) + ((level-stolen_levels) * 50) + 100
        stolen_levels = stolen_levels - 1
    
    percent_to_next_lvl = ((user.exp - current_level_required_exp) / (required_exp - current_level_required_exp)) * 100
    
    # Run the conversion function
    await fotographer.convert_html_to_png(user.level, user.exp, percent_to_next_lvl)
    
    file = discord.File("././output.png")
    
    await message.edit_original_response(content= ctx.author.mention + " calculation complete!", file=file)