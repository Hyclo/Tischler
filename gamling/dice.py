import discord
import distrib
import pentester
import random

async def dice(ctx, value, bot):
    if await pentester.check_user(ctx, ctx.author) == False:
        return
    
    user = distrib.get_user(ctx.author.id)
    
    if await pentester.check_value(ctx, user.money , value, None) == False:
        return
    
    if await pentester.value_below_zero(ctx, value) == False:
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
        distrib.add_up_value(ctx.author.id, "money", value)
    else:
        embed = discord.Embed(
            title="402 Payment Required",
            description="Just kidding " + ctx.author.mention + " you're just bad at throwing dice",
            color=discord.Colour.dark_red()
        )
        await distrib.subtract_value(ctx.author.id, "money", value)
        
    embed.add_field(name="Schreiners dice", value=str(schreiner_value))
    embed.add_field(name="Your dice", value=str(user_value))
    embed.add_field(name="Your bet", value=str(value))
        
    await ctx.respond(embed=embed)


async def online_dice(ctx, requestee, requested, value):

    DB_requested = distrib.get(requested.id)
    await pentester.check_value(ctx, DB_requested.money, value, [requested])

    DB_requestee = distrib.get(requestee.id)
    await pentester.check_value(ctx, DB_requestee.money, value, [requestee])

    requestee_value = random.randint(1,6)
    requested_value = random.randint(1,6)
    
    if requestee_value == requested_value:
        embed = discord.Embed(
            title="Result",
            description= "<@" + str(requestee.id) + " and <@" +str(requested.id)+ "> both diced the same value",
            color=discord.Colour.blurple()
        )
    elif requestee_value > requested_value:
        embed = discord.Embed(
            title="Game Result",
            description="<@" + str(requestee.id) + "> won and scammed " +str(value)+ "$ of <@" +str(requested.id)+ ">",
            color=discord.Colour.blurple()
        )
        distrib.add_up_value(requestee.id, "money", value)
        distrib.subtract_value(requested.id, "money", value)
    else:
        embed = discord.Embed(
            title="Game Result",
            description="<@" +str(requested.id)+ "> won and scammed " +str(value)+ "$ of <@" + str(requestee.id) + ">",
            color=discord.Colour.blurple()
        )
        distrib.add_up_value(requested.id, "money", value)
        distrib.subtract_value(requestee.id, "money", value)
        
    embed.add_field(name=requestee.display_name + "'s dice", value=str(requestee_value))
    embed.add_field(name=requested.display_name + "'s dice", value=str(requested_value))
    embed.add_field(name="The bet", value=str(value))
        
    await ctx.respond(embed=embed)