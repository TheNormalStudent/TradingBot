import sqlite3
from datetime import datetime, date, time


#создаём класс db_manager_cl
class db_manager_cl: 
    #создаём метод add_to_db(возвращает строку)
    def add_to_db(self):       
        con = sqlite3.connect('app/data/data.db')
        cursor = con.cursor() 
        time = datetime.now()
        data_to_db = []
        data = {"ticker":"BTCUSDT", "price": 70000, "date": time}
        for value in data.values():
            data_to_db.append(value)
        cursor.execute('''INSERT INTO crypto_info (ticker, price, date) VALUES (?,?,?)''', data_to_db)
        results = cursor.fetchall()
        con.commit()
        con.close()
        return results


    #создаём метод pull_from_db(возвращает строку)
    def pull_from_db(self):
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

