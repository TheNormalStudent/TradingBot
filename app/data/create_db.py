'''Этот файл создаёт базу данных'''



import sqlite3                                                                                          #подключение СУБД
con = sqlite3.connect('app/data/data.db')                                                               #подключение БД
cursor = con.cursor()                                                                                   #Объект выполняющий функции из базы данных 

                                                                                                        #переменная sql_query является SQL запросом
sql_query = '''                                                                                         
        CREATE TABLE crypto_info(id INTEGER PRIMARY KEY, ticker TEXT, price INTEGER,  date TEXT);
        '''
cursor.execute(sql_query)                                                                               #отправка запроса SQL
con.commit()                                                                                            #подтверждение изменений 
con.close()                                                                                             #закрытие соеденения с БД
        