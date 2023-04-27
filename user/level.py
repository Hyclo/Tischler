import pentester
import distributioner
import datetime
import random
import discord

def get_difference_in_hours(date_1):
    date_format_str = "%Y-%m-%d %H:%M"

    now = datetime.datetime.now()
        
    now = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M")
    
    start = datetime.datetime.strptime(date_1, date_format_str)
    end =   datetime.datetime.strptime(now, date_format_str)
    # Get interval between two timstamps as timedelta object
    diff = end - start
    # Get interval between two timstamps in hours
    diff_in_minutes = diff.total_seconds() / 60
    
    return diff_in_minutes

async def level(author_id, message, bot):
    
    if await pentester.is_user_in_db(author_id) == False:
        return
    
    if get_difference_in_hours(distributioner.get(author_id, "timestamplevel")) < 1:
        return
    else:
        distributioner.update(author_id, "timestamplevel" ,datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M"))
        
        distributioner.add(author_id, "exp", random.randint(15,25))
        
        level = int(distributioner.get(author_id, "level"))
        exp = distributioner.get(author_id, "exp")
        
        result = 0
        stolen_levels = level
        while stolen_levels >= 0:
            result += 5 * ((level-stolen_levels) ** 2) + ((level-stolen_levels) * 50) + 100
            stolen_levels = stolen_levels - 1
        
        if exp >= result:
            
            distributioner.add(author_id, "level", 1)
            
            ctx = await discord.Bot.get_application_context(self=bot, interaction=message.interaction, cls=discord.ApplicationContext)
            ctx.respond("You have reached a new Level", ephemeral=True)