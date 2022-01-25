import csv
from data.config import *
import csv
from binance import Client
from datetime import datetime, date, time

client = Client(API_KEY, API_SECRET)

class Parsers:
    ticker ="BTCUSDT"
    
    candles = client.get_klines(symbol=ticker, interval=Client.KLINE_INTERVAL_1MINUTE)
    last_candle = candles[499]
    
    unix_time = str(last_candle[0])
    open_time_human = datetime.utcfromtimestamp(int(unix_time[0:10])).strftime('%Y-%m-%d %H:%M:%S')

    unix_time = str(last_candle[6])
    close_time_human = datetime.utcfromtimestamp(int(unix_time[0:10])).strftime('%Y-%m-%d %H:%M:%S')

    interval = "1MIN"
    data = {"ticker":ticker, 'timeframe':interval, 'open_price':last_candle[1] , 'close_price':last_candle[4] , "max":last_candle[2] , "min":last_candle[3] , "open_date": open_time_human, "close_date": close_time_human}