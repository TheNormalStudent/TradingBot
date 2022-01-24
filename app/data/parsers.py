import csv
from config import *
import csv
import sqlite3
from binance import Client

client = Client(API_KEY, API_SECRET)


csvfile = open('app/data/2012-2020.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2019", "1 Jan, 2020")
for candlestick in candlesticks:  
    candlestick_writer.writerow(candlestick)   
csvfile.close() 