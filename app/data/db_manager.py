import sqlite3
import pandas
from data.abstract_storage_manager import AbstractStorageManager


class DbManagerCl(AbstractStorageManager):
    def __init__(self) -> None:
        super().__init__()
        self.__create_db()

# public method to use __add_to_db

    def __make_connection(self):
        with sqlite3.connect('app/data/data.db') as connection:
            return connection

    def get_data(self):
        result = self.__read()
        return result

# public method to use __pull_from_db

    def push_data(self, candle_data):
        self.__write(candle_data)

    def get_by_date(self, ticker, tics, date):
        con = self.__make_connection()
        cursor = con.cursor()
        cursor.execute('''
                          SELECT *
                          FROM crypto_info
                          WHERE open_date <= :open_date
                          AND ticker = :ticker
                          LIMIT :limit
                          ''', {'ticker': ticker, 'open_date': date, 'limit': tics})

        results = cursor.fetchall()
        con.commit()
        return results

    def to_pandas_dataframe(self, data): # tabelize the data

        to_df = {"ticker": [res_tuple[1] for res_tuple in data],
        "timeframe": [res_tuple[2] for res_tuple in data],
        "open_price": [res_tuple[3] for res_tuple in data],
        "close_price": [res_tuple[4] for res_tuple in data],
        "max": [res_tuple[5] for res_tuple in data],
        "min": [res_tuple[6] for res_tuple in data],
        "open_date": [res_tuple[7] for res_tuple in data]}
        # print(to_df)

        df = pandas.DataFrame(to_df)

        # tests:
        # ticker_df = df["ticker"]
        # print(ticker_df[0])
        # print(df)

        return df

# private method to create table and   DB

    def __create_db(self):
        con = self.__make_connection()
        cursor = con.cursor()
        sql_query = '''
            CREATE TABLE IF NOT EXISTS crypto_info
            (id INTEGER PRIMARY KEY, ticker TEXT, timeframe TEXT,
            open_price INTEGER,
            close_price INTEGER, max INTEGER, min INTEGER, open_date INTEGER);
            '''
        cursor.execute(sql_query)
        con.commit()


    def __write(self, candle_data):
        con = self.__make_connection()
        cursor = con.cursor()              
        cursor.execute('''INSERT INTO crypto_info
                          (ticker, timeframe, open_price,
                          close_price, max, min, open_date)
                          VALUES (?,?,?,?,?,?,?)''', candle_data)
        con.commit()

# private method to get info; returns *

    def __read(self):
        con = self.__make_connection()
        cursor = con.cursor()
        sql_query = '''
                SELECT * FROM [crypto_info]
                '''
        cursor.execute(sql_query)
        results = cursor.fetchall()
        con.commit()
        return results
