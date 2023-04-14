import json
import distributioner
import discord

async def migrate(ctx, key, value):
    
    if await distributioner.check_lenillian(ctx) == False:
        return
    
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            user[key] = value

    embed = discord.Embed(
        title="Migration",
        description= ctx.author.mention + " added " + key + " as new DB item!",
        color=discord.Colour.fuchsia()
    )  
    
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

    await ctx.respond(embed=embed)

        
