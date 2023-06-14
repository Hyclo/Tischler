class DB_User:
  def __init__(self, user_id, money, level, exp, timestampdaily, timestampwork, timestamplevel, working):
    self.user_id = user_id
    self.money = money
    self.level = level
    self.exp = exp
    self.timestampdaily = timestampdaily
    self.timestampwork = timestampwork
    self.timestamplevel = timestamplevel
    self.working = working

class DB_Request:
  def __init__(self, requestee, requested, betting_amount, state):
    self.requestee = requestee
    self.requested = requested
    self.betting_amount = betting_amount
    self.state = state

class DB_Stock:
  def __init__(self, stock_name, stock_value):
    self.stock_name = stock_name
    self.stock_value = stock_value

class DB_Buyer:
  def __init__(self, stock_id, user_id, count):
    self.stock_id = stock_id
    self.user_id = user_id
    self.count = count