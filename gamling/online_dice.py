import discord
import gamling.dice
import distributioner
import json

def new_request(requestee, requested, betting_amount):
    with open('online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        dict = {
            "requestee": requestee,
            "requested": requested,
            "betting_amount": betting_amount
        }

        requests.append(dict)

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

def check_requestee(requestee):
    with open('online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        for request in requests:
            if request['requestee'] == requestee:
                return False

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

    return True


def check_requested(requested):
    with open('online_dice.json') as json_file:
        data = json.load(json_file)
        
        requests = data['requests']

        for request in requests:
            if request['requested'] == requested:
                return False

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

    return True

async def send_request(ctx, member, betting_amount):

    if check_requestee(ctx.author.id) == False:
        return
    
    if check_requested(member.id) == False:
        return

    new_request(requestee=ctx.author.id, requested=member.id, betting_amount=betting_amount)

    embed = discord.Embed(
        title="dice challenge",
        description=ctx.author.mention + " challenged <@" + str(member.id) + "> to game of dice",
        color=discord.Colour.blurple()
    )

    ctx.respond(embed=embed)