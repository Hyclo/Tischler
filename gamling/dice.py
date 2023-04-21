import discord
import distributioner
import random

async def dice(ctx, value):
    
    if await distributioner.check_user(ctx) == False:
        return
    
    balance = distributioner.get(ctx.author.id, "money")
    
    if await distributioner.check_value(ctx, balance, value) == False:
        return
    
    user_value = random.randint(1,6)
    schreiner_value = random.randint(1,6)
    
    if user_value == schreiner_value:
        embed = discord.Embed(
            title="501 Not Implemented",
            description="Just kidding " + ctx.author.mention + " we threw the same so lets keep what we bet!",
            color=discord.Colour.dark_grey()
        )
        embed.add_field(name="Schreiners dice", value=str(schreiner_value))
        embed.add_field(name="Your dice", value=str(user_value))
    elif user_value > schreiner_value:
        embed = discord.Embed(
            title="You won!",
            description=ctx.author.mention + " damn you are just to good at this game...",
            color=discord.Colour.green()
        )
        distributioner.add(ctx.author.id, "money", value)
        embed.add_field(name="Schreiners dice", value=str(schreiner_value))
        embed.add_field(name="Your dice", value=str(user_value))
        embed.add_field(name="Your profit", value=str(value))
    else:
        embed = discord.Embed(
            title="402 Payment Required",
            description="Just kidding " + ctx.author.mention + " you're just bad at throwing dice",
            color=discord.Colour.dark_red()
        )
        await distributioner.subtract(ctx.author.id, "money", value)
        embed.add_field(name="Schreiners dice", value=str(schreiner_value))
        embed.add_field(name="Your dice", value=str(user_value))
        embed.add_field(name="Your loss", value=str(value))
        
    
    await ctx.respond(embed=embed)
    
    