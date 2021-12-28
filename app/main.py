from data.db_manager import db_manager_cl  #импортируем класс

db_manager = db_manager_cl()               #создаём объект класса db_manager_cl
db_manager.add_to_db()
print(db_manager.pull_from_db())