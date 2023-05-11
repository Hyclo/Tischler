import discord
import distributioner
import pentester

async def balance(ctx):
    
    if await pentester.check_user(ctx.author) == False:
        return
    
    embed = discord.Embed(
        title="Balance",
        description= ctx.author.mention + " your current balance is: " + str(distributioner.get(ctx.author.id, "money")),
        color=discord.Colour.blurple()
    )
    
    await ctx.respond(embed=embed)