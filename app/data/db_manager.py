import sqlite3



#создаём класс db_manager_cl
class db_manager_cl: 
    #создаём метод add_to_db(возвращает строку)
    def add_to_db(self):
        con = sqlite3.connect('app/data/data.db')
        cursor = con.cursor()
        sql_query ='''
        INSERT INTO crypto_info (ticker, price)
        VALUES ('BTCUSDT', 68000)
        '''
        cursor.execute(sql_query)
        con.commit()
        con.close

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

