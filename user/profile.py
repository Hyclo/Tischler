import discord
import distributioner

async def profile(ctx, bot):
    
    if await distributioner.check_user(ctx) == False:
        return
    
    user = distributioner.get_user(ctx.author.id)
    
    embed = discord.Embed(
        title="Profile",
        description= ctx.author.mention + "'s profile\r\n\r\n",
        color=discord.Colour.blurple()
    ) 
    
    embed.add_field(name="Stolen information", value="this is stolen information about this user. This user was created at " 
                    + str(ctx.author.created_at) + " and the discord id is " 
                    + str(ctx.author.id), inline=False)
    
    for key, value in user.items():
        if key == "user":
            embed.add_field(name=key, value=str(await discord.Bot.get_or_fetch_user(bot, value)), inline=True)
        else:
            embed.add_field(name=key, value=value, inline=True)
         
    embed.set_thumbnail(url=ctx.author.display_avatar)
         
    await ctx.respond(embed=embed)