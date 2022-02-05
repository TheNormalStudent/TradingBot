import sqlite3
from data.parsers import Parsers
from data.abstract_storage_manager import abstract_storage_Manager
# Айди, тикер, таймфрейм, цена открытия, цена закрытия, максимум, минимум, дата

class DB_manager_cl(abstract_storage_Manager):
    def __create_db(self):                                                                             #private method to create table and DB        
        con = sqlite3.connect('app/data/data.db')
        cursor = con.cursor() 
        sql_query = '''                                                                                         
            CREATE TABLE crypto_info(id INTEGER PRIMARY KEY, ticker TEXT, timeframe TEXT,  open_price INTEGER, close_price INTEGER, max INTEGER, min INTEGER, open_date TEXT, close_date TEXT);
            '''
        cursor.execute(sql_query)
        con.commit()
        con.close() 
    
    def __write(self):
        parsers = Parsers()
        data = parsers.save_historical_data()                                                                   #private method to add main.data to DB 
        con = sqlite3.connect('app/data/data.db')
        cursor = con.cursor()                   
        data_to_db = []
        for value in data.values():
            data_to_db.append(value)
        cursor.execute('''INSERT INTO crypto_info (ticker, timeframe, open_price, close_price, max, min, open_date, close_date) VALUES (?,?,?,?,?,?,?,?)''', data_to_db)
        con.commit()
        con.close()
    
    def __read(self):                                                                          #private method to get info returns *
        con = sqlite3.connect('app/data/data.db')
        cursor = con.cursor() 
        sql_query ='''
                SELECT * FROM [crypto_info] 
                '''
        cursor.execute(sql_query)
        results = cursor.fetchall()
        con.commit()
        con.close()
        return results

    def get_data(self):                                                                                #public method to use __add_to_db
        result = self.__read()
        return result
    def push_data(self):                                                                                #public method to use __pull_from_db
        self.__write()
    

