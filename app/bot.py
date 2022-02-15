from user import User
from data.db_manager import DB_manager_cl
from data.csv_manager import csv_Manager

class Bot:
    def __init__(self):
        self.user = User()
        self.manager = DB_manager_cl()
        self.manager_2 = csv_Manager()

    def push(self):
        self.user.binance_manager.save_historical_data()
    
    def get(self):
        print("DataBase")
        print(self.manager.get_data())
        print("CSV")
        print(self.manager_2.get_data())
    
    def __create(self):
        self.manager.create_db()
        print("created")

    
 