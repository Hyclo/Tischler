import discord
import distributioner
import pentester
import random
from datetime import timedelta
from datetime import datetime

async def dice(ctx, value, bot):
    
    if await pentester.check_user(ctx) == False:
        return
    
    balance = distributioner.get(ctx.author.id, "money")
    
    if await pentester.check_value(ctx, balance, value) == False:
        return
    
    if pentester.value_below_zero(ctx, value) == False:
        return

    user_value = random.randint(1,6)
    schreiner_value = random.randint(1,6)
    
    if user_value == schreiner_value:
        embed = discord.Embed(
            title="501 Not Implemented",
            description="Just kidding " + ctx.author.mention + " we threw the same so lets keep what we bet!",
            color=discord.Colour.dark_grey()
        )
    elif user_value > schreiner_value:
        embed = discord.Embed(
            title="You won!",
            description=ctx.author.mention + " damn you are just to good at this game...",
            color=discord.Colour.green()
        )
        distributioner.add(ctx.author.id, "money", value)
    else:
        embed = discord.Embed(
            title="402 Payment Required",
            description="Just kidding " + ctx.author.mention + " you're just bad at throwing dice",
            color=discord.Colour.dark_red()
        )
        await distributioner.subtract(ctx.author.id, "money", value)
        
    embed.add_field(name="Schreiners dice", value=str(schreiner_value))
    embed.add_field(name="Your dice", value=str(user_value))
    embed.add_field(name="Your bet", value=str(value))
        
    await ctx.respond(embed=embed)
    
    