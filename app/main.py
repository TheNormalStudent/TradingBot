'''Валюты, которыми я обычно торгую BTC, BNB, ETH, LINK, DOT'''


from data.db_manager import *              #class import
from datetime import datetime, date, time
import time

db_manager = DB_manager_cl()                               #create db_manager_cl object

db_manager.push_data()                                 #add data to DB                             
print(db_manager.get_data())                               #get data from DB