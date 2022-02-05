import csv
from data.config import *
from data.db_manager import *
import csv
from binance import Client
from datetime import datetime, date, time



class Parsers:

    def __init__(self, API, SECRET_KEY):
        __manager = DB_manager_cl()
        __client = Client(API, SECRET_KEY)
    
    def save_historical_data(self):
        ticker ="BTCUSDT"
        candles = self.__client.get_klines(symbol=ticker, interval=Client.KLINE_INTERVAL_1MINUTE)
        self.create_dict(candles[499], ticker)
    

    def create_dict(self, last_candle, ticker):
    
        unix_time = str(last_candle[0])
        open_time_human = datetime.utcfromtimestamp(int(unix_time[0:10])).strftime('%Y-%m-%d %H:%M:%S')

        unix_time = str(last_candle[6])
        close_time_human = datetime.utcfromtimestamp(int(unix_time[0:10])).strftime('%Y-%m-%d %H:%M:%S')

        interval = "1MIN"
        data = {"ticker":ticker, 'timeframe':interval, 'open_price':last_candle[1] , 'close_price':last_candle[4] , "max":last_candle[2] , "min":last_candle[3] , "open_date": open_time_human, "close_date": close_time_human} #data for DB to use
        return data
        