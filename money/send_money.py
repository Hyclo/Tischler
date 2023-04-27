import discord
import distributioner
from datetime import timedelta
from datetime import datetime


async def send_money(ctx, value,  member, bot):
    
    if await distributioner.check_user(ctx) == False:
        return
    
    if await distributioner.is_user_in_db(member.id) == False:
        embed = discord.Embed(
            title="418 I'm a teapot",
            description= "Just kidding " + "<@" + str(member.id) + ">" + " needs to use /login first to get a Job...",
            color=discord.Colour.dark_red()
        )
        
        await ctx.respond(embed=embed)
        return
        
    if value <= 0:
        embed = discord.Embed(
            title="Cringe",
            description= ctx.author.mention + " tries to spawn money he will be timeouted for a minute!",
            color=discord.Colour.dark_red()
        )
        guild = discord.Client.get_guild(bot, 908337305759141948)
    
        this_member = guild.get_member(ctx.author.id)

        await this_member.timeout((datetime.now() + timedelta(minutes=5)), "cringe bro was willsh eif geld spawne!")
    else:
        
        await distributioner.subtract(ctx.author.id, "money", value)
        
        distributioner.add(member.id, "money", value)
        
        embed = discord.Embed(
            title="Money Transfer",
            description= ctx.author.mention + " has sent " + str(value) + " to <@" + str(member.id) + ">",
            color=discord.Colour.brand_green()
        )
    
    await ctx.respond(embed=embed)
    