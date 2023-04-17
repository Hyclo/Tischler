import json
import discord

async def check_lenillian(ctx):
    if ctx.author.id == 646782364676128781:
        return True
    else:
        embed = discord.Embed(
            title="401 Unauthorized",
            description=ctx.author.mention + " you are not allowed to use owner command!",
            color=discord.Colour.dark_red()
        ) 
        
        await ctx.respond(embed=embed)
        return False
        

async def check_value(ctx, key_value, value):
    if key_value - value < 0:
        
        embed = discord.Embed(
            title="500 Internal Server Error",
            description= "Just kidding " + ctx.author.mention + " you are just too broke...",
            color=discord.Colour.dark_red()
        )   
        await ctx.respond(embed=embed)
        return False
    else:
        return True
    
async def is_user_in_db(author_id):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']
        check = False
        for user in users:
            if user['user'] == author_id:
                check = True
            
    return check
    
async def check_user(ctx):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']
        check = False
        for user in users:
            if user['user'] == ctx.author.id:
                check = True
                
        if check == False:
            embed = discord.Embed(
                title="418 I'm a teapot",
                description= "Just kidding " + ctx.author.mention + " use /login first to create get a Job...",
                color=discord.Colour.dark_red()
            )
            
            await ctx.respond(embed=embed)
            
    return check
        
def update(user_id, key, value):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            if user['user'] == user_id:
                user[key] = value

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)


def add(user_id, key, value):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            if user['user'] == user_id:
                user[key] =  user[key] + value
        
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

def get_user(user_id):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            if user['user'] == user_id:
                return user  


def get(user_id, key):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            if user['user'] == user_id:
                return user[key]


async def subtract(user_id, key, value):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            if user['user'] == user_id:
                user[key] =  user[key] - value
                

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)
        
  
async def get_multiple(key, reversed):
    
    list_of_users = {}
    
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            list_of_users[user["user"]] = user[key]
            
    return sorted(list_of_users.items(), key=lambda x:x[1], reverse=reversed)
            
                