from bot import Bot

# from data.db_manager import DB_manager_cl                  #class import

# db_manager = DB_manager_cl()                               #create db_manager_cl object
bot = Bot()
bot.push()
bot.get()


# db_manager.push_data()                                     #add data to DB                             
# print(db_manager.get_data())                               #get data from DB