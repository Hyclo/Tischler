import json
import discord

async def enter_guild(ctx, bot):
    with open('guild.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']
        check = False
        for user in users:
            if user['user'] == ctx.author.id:
                check = True

        if check == False:
            dict = {
                "user": ctx.author.id,
                "class": "human",
                "weapon": "stick",
                "armor": "old shirt",
                "level": 0,
                "exp": 0,
                "strength": 10
            }   
            users.append(dict)

            embed = discord.Embed(
                    title="Guild",
                    description=ctx.author.mention + " you successfuly entered the **guild of Azdargel**",
                    color=discord.Colour.dark_purple()
            )

        else:

            embed = discord.Embed(
                    title="login",
                    description=ctx.author.mention + " you already are an adventurer",
                    color=discord.Colour.dark_purple()
            )

    with open("guild.json", "w") as outfile:
        json.dump(data, outfile)
    
    guild = discord.Client.get_guild(bot, 908337305759141948)
    
    member = guild.get_member(ctx.author.id)
    
    role = guild.get_role(1097537972955521064)
    
    await member.add_roles(role)    

    await ctx.respond(embed=embed)

        
