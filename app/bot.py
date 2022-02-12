from user import User
from data.db_manager import DB_manager_cl

class Bot:
    def __init__(self):
        self.user = User()
        self.manager = DB_manager_cl()

    def start_some_stuff(self):
        self.user.binance_manager.save_historical_data()
    
    def get_some_stuff(self):
        print(self.manager.get_data())
    
    def __create_some_stuff(self):
        self.manager.create_db()
        print("created")

    
