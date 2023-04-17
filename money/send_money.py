import discord
import distributioner

async def send_money(ctx, value,  member):
    
    if distributioner.check_user(ctx) == False:
        return
    
    if distributioner.is_user_in_db(member.id) == False:
        embed = discord.Embed(
            title="418 I'm a teapot",
            description= "Just kidding " + ctx.author.mention + " needs to use /login first to get a Job...",
            color=discord.Colour.dark_red()
        )
        
        await ctx.respond(embed=embed)
    
    distributioner.subtract(ctx.author.id, "money", value)
    
    distributioner.add(member.id, "money", value)
    
    embed = discord.Embed(
        title="Money Transfer",
        description= ctx.author.mention + " has sent " + str(value) + " to <@" + str(member.id) + ">",
        color=discord.Colour.brand_green()
    )
    
    await ctx.respond(embed=embed)
    