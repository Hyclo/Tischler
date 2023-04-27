import distributioner
import discord
import random
import datetime
import pentester

async def daily(ctx):
    
    timestamp = str(distributioner.get(ctx.author.id, "timestampdaily"))
    
    if timestamp != str(datetime.date.today()):
    
        money = random.randint(50, 250)
        
        if await pentester.check_user(ctx) == False:
            return
        
        distributioner.add(ctx.author.id, "money", money)
        distributioner.update(ctx.author.id, "timestampdaily", str(datetime.date.today()))
        
        embed = discord.Embed(
            title="Daily",
            description= ctx.author.mention + " got his daily salary!",
            color=discord.Colour.blurple()
        )
        embed.add_field(name="Salary", value="Your Salary today is: " + str(money))
        embed.add_field(name="Balance", value="Your balance is currently at: " + str(distributioner.get(ctx.author.id, "money")))
    
    else:
        
        embed = discord.Embed(
            title="403 Forbidden",
            description= "Just kidding " + ctx.author.mention + " you already got your daily salary you greedy bitch...",
            color=discord.Colour.dark_red()
        )
        
    await ctx.respond(embed=embed)
    
    