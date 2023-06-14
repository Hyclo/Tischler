import mariadb
import DB_Objects
import datetime.datetime as dt

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
    
    return None

def get_all_users():
    con.cur.execute("SELECT * FROM users")

    list_of_users = []

    for (user_id, money, level, exp, timestampdaily, timestampwork, timestamplevel, working) in con.cur:
        list_of_users.append(DB_Objects.DB_User(user_id, money, level, exp, timestampdaily, timestampwork, timestamplevel, working))

    return list_of_users

def add_user(user_id):
    money = 1000
    level = 0
    exp = 0
    timestampdaily = str(dt.date.today() - dt.timedelta(days=1))
    timestampwork = dt.strftime(dt.now() - dt.timedelta(days=1), "%Y-%m-%d %H:%M")
    timestamplevel = dt.strftime(dt.now() - dt.timedelta(days=1), "%Y-%m-%d %H:%M")
    working = False

    con.cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (user_id, money, level, exp, timestampdaily, timestampwork, timestamplevel, working))

def delete_user(user_id):
    con.cur.execute("DELETE FROM users WHERE user_id=?", (user_id))

def get_stock(stock_name):
    con.cur.execute("SELECT * FROM stocks WHERE stock_name=?", (stock_name))

    for (stock_name, stock_value) in con.cur:
        return DB_Objects.DB_Stock(stock_name, stock_value)
    
    return None

def get_all_stocks():
    con.cur.execute("SELECT * FROM stocks")

    list_of_stocks = []

    for (stock_name, stock_value) in con.cur:
        list_of_stocks.append(DB_Objects.DB_Stock(stock_name, stock_value))

    return list_of_stocks

def add_stock(stock_name, stock_value):
    con.cur.execute("INSERT INTO stocks VALUES (?, ?)", (stock_name, stock_value))

def add_up_value(user_id, key, value):
    con.cur.execute("UPDATE users SET ? = ? + ? WHERE user_id=?", (key, key, value, user_id))

def subtract_value(user_id, key, value):
    con.cur.execute("UPDATE users SET ? = ? - ? WHERE user_id=?", (key, key, value, user_id))

def update(user_id, key, value):
    con.cur.execute("UPDATE users SET ? = ? WHERE user_id=?", (key, value, user_id))

def get_request(requestee_id, requested_id):
    wanted_state = "pending"
    con.cur.execute("SELECT * FROM requests WHERE requestee=? AND requested=? AND state=?", (requestee_id, requested_id, wanted_state))

    for (requestee, requested, betting_amount, state) in con.cur:
        return DB_Objects.DB_Request(requestee, requested, betting_amount, state)
    
    return None

def delete_request(requestee_id, requested_id):
    wanted_state = "done"
    con.cur.execute("UPDATE requests SET state=? WHERE requestee=? AND requested=?", (wanted_state, requestee_id, requested_id))

def add_request(requestee_id, requested_id, betting_amount):
    state = "pending"
    con.cur.execute("INSERT INTO requests VALUES (?, ?, ?, ?)", (requestee_id, requested_id, betting_amount, state))

def get_buyer(buyer_id, stock_name):
    con.cur.execute("SELECT * FROM buyers WHERE user_id=? AND stock_name=?", (buyer_id, stock_name))

    for (user_id, stock_name, stock_amount) in con.cur:
        return DB_Objects.DB_Buyer(user_id, stock_name, stock_amount)
    
    return None

def delete_buyer(buyer_id, stock_name):
    con.cur.execute("DELETE FROM buyers WHERE user_id=? AND stock_name=?", (buyer_id, stock_name))

def add_buyer(buyer_id, stock_name, stock_amount):
    con.cur.execute("INSERT INTO buyers VALUES (?, ?, ?)", (buyer_id, stock_name, stock_amount))

def add_buyer_stock(buyer_id, stock_name, amount):
    con.cur.execute("UPDATE buyers SET stock_amount = stock_amount + ? WHERE user_id=? AND stock_name=?", (amount, buyer_id, stock_name))

def subtract_buyer_stock(buyer_id, stock_name, amount):
    con.cur.execute("UPDATE buyers SET stock_amount = stock_amount - ? WHERE user_id=? AND stock_name=?", (amount, buyer_id, stock_name))
