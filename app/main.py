from data.db_manager import DB_manager_cl                  #class import
from datetime import datetime, date, time

db_manager = DB_manager_cl()                               #create db_manager_cl object
timel = datetime.now()
data = {"ticker":"BTCUSDT", "price": 69000, "date": timel} #data to DB
db_manager.push_data(data)                                 #add data to DB                             
print(db_manager.get_data())                               #get data from DB