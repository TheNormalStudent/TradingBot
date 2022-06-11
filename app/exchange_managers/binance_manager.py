from data.db_manager import DB_manager_cl
from binance import Client
from data.csv_manager import csv_Manager


class Binance_manager:

    def __init__(self, API, SECRET_KEY, TRADINGLIST):
        self.__tickerlist = TRADINGLIST
        self.__manager = DB_manager_cl()
        self.__csv_manager = csv_Manager()
        self.__client = Client(API, SECRET_KEY)

    def save_historical_data(self):

        for ticker in self.__tickerlist:
            print(ticker)
            candles = self.__client.get_klines(symbol=ticker, interval=Client.KLINE_INTERVAL_1MINUTE)
            for candle in candles:
                candle = self.create_dict(candle, ticker)
                self.__manager.push_data(candle)
                self.__csv_manager.push_data(candle)

    def create_dict(self, candle, ticker):
        interval = "1MIN"
        data = {"ticker": ticker, 'timeframe': interval,
                'open_price': candle[1],'close_price': candle[4],
                "max": candle[2], "min": candle[3],
                "open_date": candle[0]}  # data for DB to use
        candle_data = []
        for value in data.values():
            candle_data.append(value)
        return candle_data

    def check_balance(self):
        balance = self.__client.get_asset_balance(asset='USDT')
        print(balance)

    def buy(symbol, quantity, price, self):
        # order= self.__client.order_limit_buy(symbol, quantity, price)
        print(symbol)
        print(quantity)
        print(price)
        print("bought this stuff")

    def sell(symbol, quantity, price, self):
        # order= self.__client.order_limit_sell(symbol, quantity, price)
        print(symbol)
        print(quantity)
        print(price)
        print("sold this stuff")
