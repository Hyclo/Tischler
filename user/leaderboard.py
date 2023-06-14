import discord
import distrib


async def leaderboard(ctx, bot):
    embed = discord.Embed(
            title="Forbes 3",
            description= ctx.author.mention + " wanted to see the three richest tischlers",
            color=discord.Colour.dark_gold()
    )
    
    users = await distrib.get_all_users()

    users.sort(key=lambda x: x[1], reverse=True)
    
    embed.add_field(name="Top 1", value=str(await discord.Bot.get_or_fetch_user(bot, users[0][0])) + " with " + str(users[0][1]))
    embed.add_field(name="Top 2", value=str(await discord.Bot.get_or_fetch_user(bot, users[1][0])) + " with " + str(users[1][1]))
    embed.add_field(name="Top 3", value=str(await discord.Bot.get_or_fetch_user(bot, users[2][0])) + " with " + str(users[2][1]))
    
    
    await ctx.respond(embed=embed)