import sqlite3
from datetime import datetime, date, time
date = datetime.now()

con = sqlite3.connect('app/data/data.db')
cursor = con.cursor() 
sql_query = '''
        CREATE TABLE crypto_info(id INTEGER PRIMARY KEY, ticker TEXT, price INTEGER);
        '''
sql_query_2 ='''
        INSERT INTO crypto_info (ticker, price)
        VALUES ('BTCUSDT', 68000, "date")
        '''
sql_query_3 ='''
        SELECT * FROM [crypto_info] 
        '''
cursor.execute(sql_query)
results = cursor.fetchall()
print(results)
con.commit()
con.close()
