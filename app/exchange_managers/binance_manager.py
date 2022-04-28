from http.server import ThreadingHTTPServer
from data.db_manager import *
from binance import Client
from data.csv_manager import csv_Manager
from datetime import datetime

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
            candle = self.create_dict(candles[499], ticker)
            self.__manager.push_data(candle)
            self.__csv_manager.push_data(candle)
    

    def create_dict(self, last_candle, ticker):
    
        unix_time = str(last_candle[0])
        open_time_human = datetime.utcfromtimestamp(int(unix_time[0:10])).strftime('%Y-%m-%d %H:%M:%S')

        unix_time = str(last_candle[6])
        close_time_human = datetime.utcfromtimestamp(int(unix_time[0:10])).strftime('%Y-%m-%d %H:%M:%S')

        interval = "1MIN"
        data = {"ticker":ticker, 'timeframe':interval, 'open_price':last_candle[1] , 'close_price':last_candle[4] , "max":last_candle[2] , "min":last_candle[3] , "open_date": open_time_human, "close_date": close_time_human} #data for DB to use
        candle_data = []
        for value in data.values():
            candle_data.append(value)
        return candle_data
    
    def check_balance(self):
        balance = self.__client.get_asset_balance(asset='BTC')
        print(balance)
        