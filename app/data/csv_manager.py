import csv
from data.abstract_storage_manager import AbstractStorageManager


class CsvManager(AbstractStorageManager):
    def __write(self, candle_data):
        with open('app/data/info.csv', 'a', newline='') as file:
            candlestickwriter = csv.writer(file, delimiter=',')
            candlestickwriter.writerow(candle_data)

    def __read(self):                                                                         
        csv_file = open('app/data/info.csv')
        csvreader = csv.reader(csv_file)
        candlesticks = []
        for candlestick in csvreader:
            candlesticks.append(candlestick)
        csv_file.close()
        return candlesticks

    def get_data(self):                                                                             
        return self.__read()

    def push_data(self, candle_data):
        self.__write(candle_data)
