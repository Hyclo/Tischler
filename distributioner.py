import json
       
def update(user_id, key, value):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            if user['user'] == user_id:
                user[key] = value

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)


def add(user_id, key, value):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            if user['user'] == user_id:
                user[key] =  user[key] + value
        
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

def get_user(user_id):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            if user['user'] == user_id:
                return user  


def get(user_id, key):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            if user['user'] == user_id:
                return user[key]


async def subtract(user_id, key, value):
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            if user['user'] == user_id:
                user[key] =  user[key] - value
                

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)
        
  
async def get_multiple(key, reversed):
    
    list_of_users = {}
    
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        server = data['server']

        users = server['users']

        for user in users:
            list_of_users[user["user"]] = user[key]
            
    return sorted(list_of_users.items(), key=lambda x:x[1], reverse=reversed)
            
                