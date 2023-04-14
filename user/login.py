import json
import datetime
import discord
from distributioner import *

async def login(ctx, bot):
    with open('data.json') as json_file:
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
                "money": 0,
                "level": 0,
                "exp": 0,
                "timestampdaily": str(datetime.date.today() - datetime.timedelta(days=1)),
                "timestampwork": str(datetime.date.today() - datetime.timedelta(days=1))
            }   
            users.append(dict)

            embed = discord.Embed(
                    title="login",
                    description=ctx.author.mention + " your login was succsesful",
                    color=discord.Colour.blurple()
            )

        else:

            embed = discord.Embed(
                    title="login",
                    description=ctx.author.mention + " you already have an account",
                    color=discord.Colour.blurple()
            )

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)
        
    update(ctx.author.id, "money", 1000)
    
    guild = discord.Client.get_guild(bot, 908337305759141948)
    
    member = guild.get_member(ctx.author.id)
    
    role = guild.get_role(1096485229541204129)
    
    await member.add_roles(role)    

    await ctx.respond(embed=embed)

        
