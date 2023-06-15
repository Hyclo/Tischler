import discord
import pentester
import json
from gamling.dice import online_dice
from gamling.dice import dice
import distrib

async def dice_chooser(ctx, value, member, bot):
    if member != "none":
        await send_request(ctx, member, value)
    else:
        await dice(ctx, value, bot)

'''
embed = discord.Embed(
                title="449 The request should be retried after doing the appropriate action",
                description= "Just kidding " + ctx.author.mention + " this user hasn't challenged you",
                color=discord.Colour.dark_red()
            )

        embed = discord.Embed(
                title="449 The request should be retried after doing the appropriate action",
                description= "Just kidding " + ctx.author.mention + " you already challenged someone",
                color=discord.Colour.dark_red()
            )

        embed = discord.Embed(
                title="449 The request should be retried after doing the appropriate action",
                description= "Just kidding " + ctx.author.mention + ", <@" + member.id +"> is already being challenged",
                color=discord.Colour.dark_red()
            )

'''

async def send_request(ctx, member, betting_amount):

    me = distrib.get_user(ctx.author.id)

    them = distrib.get_user(member.id)

    if me == None or them:
        embed = discord.Embed(
            title="449 The request should be retried after doing the appropriate action",
            description=ctx.author.mention + " you or the person you are challenging are not in the database",
            color=discord.Colour.dark_red()
        )

        await ctx.respond(embed=embed)
        return

    distrib.add_request(ctx.author.id, member.id, betting_amount)

    embed = discord.Embed(
        title="dice challenge",
        description=ctx.author.mention + " challenged <@" + str(member.id) + "> to game of dice with a bet of: " + str(betting_amount),
        color=discord.Colour.blurple()
    )

    await ctx.respond(embed=embed)

async def accept(ctx, member):

    request = distrib.get_request(ctx.author.id, member.id)

    if request != None:
        distrib.delete_request(ctx.author.id, member.id)

        await online_dice(ctx, member, ctx.author, int(request["betting_amount"]))
        return
    else:
        embed = discord.Embed(
            title="449 The request should be retried after doing the appropriate action",
            description=ctx.author.mention + " nodbody has challenged you",
            color=discord.Colour.dark_red()
        )

        await ctx.respond(embed=embed)
        return

async def deny(ctx, member):
    request = distrib.get_request(ctx.author.id, member.id)

    if request != None:
        distrib.delete_request(ctx.author.id, member.id)
        embed = discord.Embed(
            title="dice challenge",
            description=ctx.author.mention + " declined the challenge of <@" + str(member.id) + ">",
            color=discord.Colour.blurple()
        )

        await ctx.respond(embed=embed)
        return
    else:
        embed = discord.Embed(
            title="449 The request should be retried after doing the appropriate action",
            description=ctx.author.mention + " nodbody has challenged you",
            color=discord.Colour.dark_red()
        )

        await ctx.respond(embed=embed)
        return

async def clear_requests(ctx):
    with open('gamling/online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        for request in requests:
            if request["requestee"] == ctx.author.id and request["state"] == "open":
                request["state"] = "done"

    with open("gamling/online_dice.json", "w") as outfile:
        json.dump(data, outfile)

    await ctx.respond("challenges cleared")
