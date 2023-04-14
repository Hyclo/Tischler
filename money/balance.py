import discord
import distributioner

async def balance(ctx):
    
    if await distributioner.check_user(ctx) == False:
        return
    
    embed = discord.Embed(
        title="Balance",
        description= ctx.author.mention + " your current balance is: " + str(distributioner.get(ctx.author.id, "money")),
        color=discord.Colour.blurple()
    )
    
    await ctx.respond(embed=embed)