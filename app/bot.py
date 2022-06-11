from user import User
from data.db_manager import DB_manager_cl
from data.csv_manager import csv_Manager


class Bot:
    def __init__(self):
        self.user = User()
        self.manager = DB_manager_cl()
        self.manager_2 = csv_Manager()

    def select_where(self):
        open_date = 1654703340001
        limit = 1
        self.manager.select_where(open_date, limit)

    def push_historical_data(self):
        self.user.binance_manager.save_historical_data()

    def get_historical_data(self):
        print("DataBase")
        print(self.manager.get_data())
        print("CSV")
        print(self.manager_2.get_data())

    def check_balance(self):
        self.user.binance_manager.check_balance()

    def run():
        pass

    # def create(self):
    #     self.manager.create_db()
    #     print("created")
