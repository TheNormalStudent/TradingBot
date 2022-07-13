from data.db_manager import DbManagerCl
from binance import Client
from data.csv_manager import csv_Manager
from data.config import TRADING_LIST


class BinanceManager:

    def __init__(self, API, SECRET_KEY):
        self.__manager = DbManagerCl()
        self.__csv_manager = csv_Manager()
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
        data = {"ticker": ticker, 'timeframe': interval,
                'open_price': candle[1], 'close_price': candle[4],
                "max": candle[2], "min": candle[3],
                "open_date": candle[0]}  # data for DB to use
        candle_data = []
        for value in data.values():
            candle_data.append(value)
        return candle_data

    def check_balance(self):
        balance = self.__client.get_asset_balance(asset='USDT')
        print(balance)

    def __buy_limit(symbol, quantity, price, self):
        # order= self.__client.order_limit_buy(symbol, quantity, price)
        print(symbol)
        print(quantity)
        print(price)
        print("bought this stuff")

    def __sell_limit(symbol, quantity, price, self):
        # order= self.__client.order_limit_sell(symbol, quantity, price)
        print(symbol)
        print(quantity)
        print(price)
        print("sold this stuff")

    def __market_buy(symbol, quantity, self):
        # order = self.__client.order_market_buy(symbol, quantity)
        print(symbol)
        print(quantity)
        print("Market bought some stuff")

    def __market_sell(symbol, quantity, self):
        # order = self.__client.order_market_sell(symbol, quantity)
        print(symbol)
        print(quantity)
        print("Market sold some stuff")

    def buy_lim(self, symbol, quantity, price):
        print("buy_limit")
        self.__buy_limit(symbol, quantity, price)
        print(self.__client.get_system_status())

    def sell_lim(self, symbol, quantity, price):
        print("sell_limit")
        self.__sell_limit(symbol, quantity, price)
        print(self.__client.get_system_status())

    def buy_mark(self, symbol, quantity):
        print("buy market")
        self.__market_buy(symbol, quantity)
        print(self.__client.get_system_status())

    def sell_mark(self, symbol, quantity):
        print("sell market")
        self.__market_sell(symbol, quantity)
        print(self.__client.get_system_status())
