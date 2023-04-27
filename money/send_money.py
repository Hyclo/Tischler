import discord
import distributioner
import pentester


async def send_money(ctx, value,  member, bot):
    
    if await pentester.check_user(ctx) == False:
        return
    
    if await pentester.is_user_in_db(member.id) == False:
        embed = discord.Embed(
            title="418 I'm a teapot",
            description= "Just kidding " + "<@" + str(member.id) + ">" + " needs to use /login first to get a Job...",
            color=discord.Colour.dark_red()
        )
        
        await ctx.respond(embed=embed)
        return
        
    if await pentester.value_below_zero(ctx, value) == False:
        return 
    
    await distributioner.subtract(ctx.author.id, "money", value)
    
    distributioner.add(member.id, "money", value)
    
    embed = discord.Embed(
        title="Money Transfer",
        description= ctx.author.mention + " has sent " + str(value) + " to <@" + str(member.id) + ">",
        color=discord.Colour.brand_green()
    )
    
    await ctx.respond(embed=embed)
    