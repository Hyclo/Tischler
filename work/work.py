import discord
import distributioner
import asyncio


async def start_working(ctx):
    if await distributioner.check_user(ctx) == False:
        return
    
    
    if distributioner.get(ctx.author.id, "working") == "True":
        embed = discord.Embed(
            title="406 Not Acceptable",
            description= "Just kidding " + ctx.author.mention + " but u are already working!",
            color=discord.Colour.dark_red()
        )
        await ctx.respond(embed=embed)
    else:
        distributioner.update(ctx.author.id, "working", str(True))
        
        embed = discord.Embed(
            title="Tischler",
            description=ctx.author.mention + " started working!",
            color=discord.Colour.blurple()
        )
        await ctx.respond(embed=embed)
        
        await work(ctx)
    

async def work(ctx):
    try:
        await asyncio.sleep(3600)
        
        money = 10 * (distributioner.get(ctx.author.id, "level") + 1)
        
        embed = discord.Embed(
            title="Tischler",
            description=ctx.author.mention + " you are done with work for now working!",
            color=discord.Colour.blurple()
        )
        embed.add_field(name="Money made", value=str(money), inline=True)
        
        distributioner.update(ctx.author.id, "working", str(False))
        
        distributioner.add(ctx.author.id, "money", money)
        
        await ctx.respond(embed=embed)
        
        return
    except:
        pass