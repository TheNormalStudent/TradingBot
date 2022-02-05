import csv
from data.parsers import Parsers
from data.abstract_storage_manager import abstract_storage_Manager

class csv_Manager(abstract_storage_Manager):
    
    
    def __write(self):
        parsers = Parsers()
        csv_file = open('candlesticks.csv', 'w', newline='')
        candlestickwriter = csv.writer(csv_file, delimiter=',')
        data = parsers.save_historical_data()
        candlestickwriter.writerow(data)
        csv_file.close()

    def __read(self):                                                                         
        csv_file = open("candlesticks.csv")
        csvreader = csv.reader(csv_file)
        candlesticks = []
        for candlestick in csvreader:
            candlesticks.append(candlestick)
        csv_file.close()
        return candlesticks

    def get_data(self):                                                                             
        result = self.__read()
        return result
    def push_data(self):                                                                               
        self.__write()