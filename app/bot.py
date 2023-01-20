from user import User
from data.db_manager import DbManagerCl
from data.csv_manager import CsvManager
from TA_managers.TA_manager import TaManager


class Bot:
    def __init__(self):
        self.user = User()
        self.manager = DbManagerCl()
        self.manager_2 = CsvManager()

    def select_where(self):
        open_date = 1654703340001
        limit = 1
        self.manager.get_by_date(open_date, limit)

    def push_historical_data(self):
        self.user.binance_manager.save_historical_data()

    def get_historical_data(self):
        print("DataBase")
        print(self.manager.get_data())
        print("CSV")
        print(self.manager_2.get_data())

    def check_balance(self):
        self.user.binance_manager.check_balance()

    def run(self):
        ta = TaManager()
        ta.rsi_analyse('BTCUSDT', 500, 1674160500000)





    # def pandas_test(self):
    #     self.manager.to_pandas_dataframe()


    def create(self):
        self.manager.create_db()
        print("created")
