import discord
import distributioner
import datetime
import random

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

async def level(author_id):
    
    if await distributioner.is_user_in_db(author_id) == False:
        return
    
    if get_difference_in_hours(distributioner.get(author_id, "timestamplevel")) < 1:
        return
    else:
        distributioner.update(author_id, "timestamplevel" ,datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M"))
        
        distributioner.add(author_id, "exp", random.randint(15,25))
        
        level = int(distributioner.get(author_id, "level"))
        exp = distributioner.get(author_id, "exp")
        
        if exp >= 5 * (level ** 2) + (50 * level) + 100 - exp:
            distributioner.add(author_id, "level", 1)