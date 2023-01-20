from data.db_manager import DbManagerCl
from binance import Client
from data.csv_manager import CsvManager
from data.config import TRADING_LIST


class BinanceManager:

    def __init__(self, API, SECRET_KEY):
        self.__manager = DbManagerCl()
        self.__csv_manager = CsvManager()
        self.__client = Client(API, SECRET_KEY)

    def save_historical_data(self):

        for ticker in TRADING_LIST:
            print(ticker)
            candles = self.__client.get_klines(symbol=ticker,
            interval=Client.KLINE_INTERVAL_1MINUTE) # noqa

            for candle in candles:
                candle = self.create_dict(candle, ticker)
                self.__manager.push_data(candle)
                self.__csv_manager.push_data(candle)

    def create_dict(self, candle, ticker):
        interval = "1MIN"
        candle_data = [ticker, interval, candle[1], candle[4], candle[2], candle[3], candle[0]] # candle_data = [ticker, interval, open price, close_price, max, min, open_date]
        return candle_data

    def check_balance(self):
        balance = self.__client.get_asset_balance(asset='USDT')
        print(balance)

    def buy_lim(self, symbol, quantity, price):
        #order = self.__client.order_limit_buy(symbol, quantity, price)
        print("buy_limit")
        self.__buy_limit(symbol, quantity, price)
        print(self.__client.get_system_status())

    def sell_lim(self, symbol, quantity, price):
        #order= self.__client.order_limit_sell(symbol, quantity, price)
        print("sell_limit")
        self.__sell_limit(symbol, quantity, price)
        print(self.__client.get_system_status())

    def buy_mark(self, symbol, quantity):
        #order = self.__client.order_market_buy(symbol, quantity)
        print("buy market")
        self.__market_buy(symbol, quantity)
        print(self.__client.get_system_status())

    def sell_mark(self, symbol, quantity):
        #order = self.__client.order_market_sell(symbol, quantity)
        print("sell market")
        self.__market_sell(symbol, quantity)
        print(self.__client.get_system_status())
