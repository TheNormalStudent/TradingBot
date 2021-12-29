import sqlite3
con = sqlite3.connect('app/data/data.db')
cursor = con.cursor() 

sql_query = '''
        CREATE TABLE crypto_info(id INTEGER PRIMARY KEY, ticker TEXT, price INTEGER,  date TEXT);
        '''
cursor.execute(sql_query)
con.commit()
con.close()
        