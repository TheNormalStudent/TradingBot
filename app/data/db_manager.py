import sqlite3
import pandas
from data.abstract_storage_manager import AbstractStorageManager


class DbManagerCl(AbstractStorageManager):
    def __init__(self) -> None:
        super().__init__()
        self.__create_db()

# public method to use __add_to_db
    def get_data(self):
        result = self.__read()
        return result

# public method to use __pull_from_db

    def push_data(self, candle_data):
        self.__write(candle_data)

    def get_by_date(self, date, limit):
        con = sqlite3.connect('app/data/data.db')
        cursor = con.cursor()
        cursor.execute('''
                          SELECT *
                          FROM crypto_info
                          WHERE open_date <= :open_date
                          LIMIT :limit
                          ''', {'open_date': date, 'limit': limit})

        results = cursor.fetchall()
        con.commit()
        con.close()
        print(results)

    def pandas_dataframe(self):
        con = sqlite3.connect('app/data/data.db')
        cursor = con.cursor()

        cursor.execute('''SELECT ticker, timeframe, open_price, close_price, max, min, open_date FROM crypto_info''')
        res = cursor.fetchall()
        res_normal = []
        for num in range(len(res)):
            res_tpl = res[num]
            res_lst = list(res_tpl)
            res_normal.append(res_lst)

        con.commit()
        con.close()

        data = {"ticker": [elem[0] for elem in res_normal],
        "timeframe": [elem[1] for elem in res_normal],
        "open_price": [elem[2] for elem in res_normal],
        "close_price": [elem[3] for elem in res_normal],
        "max": [elem[4] for elem in res_normal],
        "min": [elem[5] for elem in res_normal],
        "open_date": [elem[6] for elem in res_normal]}

        df = pandas.DataFrame(data)
        # ticker_df = df["ticker"]
        # print(ticker_df[0])
        print(df)

# private method to create table and DB

    def __create_db(self):
        con = sqlite3.connect('app/data/data.db')
        cursor = con.cursor()
        sql_query = '''
            CREATE TABLE IF NOT EXISTS crypto_info
            (id INTEGER PRIMARY KEY, ticker TEXT, timeframe TEXT,
            open_price INTEGER,
            close_price INTEGER, max INTEGER, min INTEGER, open_date INTEGER);
            '''
        cursor.execute(sql_query)
        con.commit()
        con.close()

    def __write(self, candle_data):
        con = sqlite3.connect('app/data/data.db')
        cursor = con.cursor()              
        cursor.execute('''INSERT INTO crypto_info
                          (ticker, timeframe, open_price,
                          close_price, max, min, open_date)
                          VALUES (?,?,?,?,?,?,?)''', candle_data)
        con.commit()
        con.close()
# private method to get info returns *

    def __read(self):
        con = sqlite3.connect('app/data/data.db')
        cursor = con.cursor()
        sql_query = '''
                SELECT * FROM [crypto_info]
                '''
        cursor.execute(sql_query)
        results = cursor.fetchall()
        con.commit()
        con.close()
        return results
