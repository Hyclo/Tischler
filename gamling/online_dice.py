import discord
from gamling.dice import online_dice
import distributioner
import pentester
import json

async def find_request(ctx, requestee, requested):
    with open('gamling/online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        open_request = {}

        for request in requests:
            if request["requestee"] == requestee and request["requested"] == requested and request["state"] == "open":
                open_request = request

        if open_request == {}:
            embed = discord.Embed(
                title="449 The request should be retried after doing the appropriate action",
                description= "Just kidding " + ctx.author.mention + " this user hasn't challenged you",
                color=discord.Colour.dark_red()
            )
            
            await ctx.respond(embed=embed)
            return False
        
        return open_request
    
def replace_request(requestee, requested, newValue):
    with open('gamling/online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        for request in requests:
            if request["requestee"] == requestee and request["requested"] == requested and request["state"] == "open":
                request = newValue

    with open("gamling/online_dice.json", "w") as outfile:
        json.dump(data, outfile)

def new_request(requestee, requested, betting_amount):
    with open('gamling/online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        dict = {
            "requestee": requestee,
            "requested": requested,
            "betting_amount": betting_amount,
            "state": "open"
        }

        requests.append(dict)

    with open("gamling/online_dice.json", "w") as outfile:
        json.dump(data, outfile)

def check_requestee(requestee):
    with open('gamling/online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        for request in requests:
            if request['requestee'] == requestee and request["state"] == "open":
                return False

    with open("gamling/online_dice.json", "w") as outfile:
        json.dump(data, outfile)

    return True

def check_requested(requested):
    with open('gamling/online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        for request in requests:
            if request['requested'] == requested and request["state"] == "open":
                return False

    with open("gamling/online_dice.json", "w") as outfile:
        json.dump(data, outfile)

    return True

async def send_request(ctx, member, betting_amount):

    if await pentester.check_user(ctx, ctx.author) == False:
        return
    
    if await pentester.check_user(ctx, member) == False:
        return

    if check_requestee(ctx.author.id) == False:
        embed = discord.Embed(
                title="449 The request should be retried after doing the appropriate action",
                description= "Just kidding " + ctx.author.mention + " you already challenged someone",
                color=discord.Colour.dark_red()
            )
            
        await ctx.respond(embed=embed)
        return
    
    if check_requested(member.id) == False:
        embed = discord.Embed(
                title="449 The request should be retried after doing the appropriate action",
                description= "Just kidding " + ctx.author.mention + ", <@" + member.id +"> is already being challenged",
                color=discord.Colour.dark_red()
            )
            
        await ctx.respond(embed=embed)
        return

    new_request(requestee=ctx.author.id, requested=member.id, betting_amount=betting_amount)

    embed = discord.Embed(
        title="dice challenge",
        description=ctx.author.mention + " challenged <@" + str(member.id) + "> to game of dice with a bet of: " + str(betting_amount),
        color=discord.Colour.blurple()
    )

    await ctx.respond(embed=embed)

async def accept(ctx, member):
    if await find_request(ctx, member.id, ctx.author.id) == False:
        return
    
    with open('gamling/online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        for request in requests:
            if request["requested"] == ctx.author.id and request["state"] == "open":
                request["state"] = "done"

    with open("gamling/online_dice.json", "w") as outfile:
        json.dump(data, outfile)

    await online_dice(ctx, member, ctx.author, int(request["betting_amount"]))
    return

async def deny(ctx, member):
    if await find_request(ctx, member.id, ctx.author.id) == False:
        return
    with open('gamling/online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        for request in requests:
            if request["requested"] == ctx.author.id and request["state"] == "open":
                request["state"] = "done"

    with open("gamling/online_dice.json", "w") as outfile:
        json.dump(data, outfile)

    embed = discord.Embed(
        title="dice challenge",
        description=ctx.author.mention + " declined the challenge of <@" + str(member.id) + ">",
        color=discord.Colour.blurple()
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
