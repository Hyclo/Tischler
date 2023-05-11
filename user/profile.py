import discord
import distributioner
import pentester

async def profile(ctx, bot, member):

    ctx_author = ctx.author

    if member != 'null':
        ctx_author = await bot.get_or_fetch_user(member.id)
    
    if await pentester.check_user(ctx, ctx_author) == False:
        return
    
    print(ctx_author.id)

    user = distributioner.get_user(ctx_author.id)
    
    embed = discord.Embed(
        title="Profile",
        description= ctx_author.mention + "'s profile\r\n\r\n",
        color=discord.Colour.blurple()
    ) 
    
    embed.add_field(name="Stolen information", value="this is stolen information about this user. This user was created at " 
                    + str(ctx_author.created_at) + " and the discord id is " 
                    + str(ctx_author.id), inline=False)
    
    for key, value in user.items():
        if key == "user":
            embed.add_field(name=key, value=str(await discord.Bot.get_or_fetch_user(bot, value)), inline=True)
        else:
            embed.add_field(name=key, value=value, inline=True)
         
    embed.set_thumbnail(url=ctx_author.display_avatar)
         
    await ctx.respond(embed=embed)