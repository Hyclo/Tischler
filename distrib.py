import mariadb
import DB_Objects

class Connector:
    def __init__(self):
        try:
            conn = mariadb.connect(
                user="root",
                password="",
                host="192.0.2.1",
                port=3306,
                database="tischler"

            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

        self.cur = conn.cursor()

con = Connector()

def get_user(user_id):
    con.cur.execute("SELECT * FROM users WHERE user_id=?", (user_id))

    for (user_id, money, level, exp, timestampdaily, timestampwork, timestamplevel, working) in con.cur:
        return DB_Objects.DB_User(user_id, money, level, exp, timestampdaily, timestampwork, timestamplevel, working)

def get_all_users():
    return

def add_user(user_id):
    return

def delete_user(user_id):
    return

def get_stock(stock_name):
    return

def get_all_stocks():
    return

def add_stock(stock_name, stock_value):
    return

def add_up_value(user_id, key, value):
    return

def subtract_value(user_id, key, value):
    return

def update(user_id, key, value):
    return

def get_request(requestee_id, requested_id):
    return

def delete_request(requestee_id, requested_id):
    return

def add_request(requestee_id, requested_id):
    return

def get_buyer(buyer_id, stock_name):
    return

def delete_buyer(buyer_id, stock_name):
    return

def add_buyer(buyer_id, stock_name, stock_amount):
    return

def add_buyer_stock(buyer_id, stock_name):
    return

def subtract_buyer_stock(buyer_id, stock_name):
    return