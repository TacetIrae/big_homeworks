import controller
import sqlite3
from controller import Person as per
import self

def first_start():
    starting = input("Привет!\n\
                     Сейчас я расскажу как работает моя база данных\n\
                     Моя база данных основана ан MySQL и я постарался реализовать несколько функиий\n\
                     Здесь будут функции такие как ввод новых данных, вывод данных, поиск данных по любым параметрам включая id\n\
                     Для того чтобы начать напишите 'start' это вызовет инициалищацию базы данных\n"
                     "").lower()
    if starting == 'start':
        connection = sqlite3.connect('workdb.db')

        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            telephone_number TEXT 
            )
            """)
        per.__init__(self)
        per.start_prog(self)
        connection.commit()
    else:
        print("Have a nice day")


first_start()
