import distrib

def is_user_in_db(user_id):
    return distrib.get_user(user_id) != None

def is_request_in_db(requestee, requested):
    return distrib.get_request(requestee, requested) != None

def is_stock_in_db(stock_name):
    return distrib.get_stock(stock_name) != None

def is_buyer_in_db(user_id, stock_name):
    return distrib.get_buyer(user_id, stock_name) != None