import csv
from data.abstract_storage_manager import abstract_storage_Manager

class csv_Manager(abstract_storage_Manager):
    
    
    def __write(self, norm_candle):
        with open('app/data/info.csv') as csv_file:
            candlestickwriter = csv.writer(csv_file, delimiter=',')
            candlestickwriter.writerow(norm_candle)    
    def __read(self):                                                                         
        with open('app/data/info.csv') as csv_file:
            csvreader = csv.reader(csv_file)
            candlesticks = []
            for candlestick in csvreader:
                candlesticks.append(candlestick)
        return candlesticks

    def get_data(self):                                                                             
        return self.__read()

    def push_data(self, norm_candle):                                                                               
        self.__write(norm_candle)