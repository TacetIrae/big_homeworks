import sqlite3

import self

connection = sqlite3.connect('workdb.db')

class Person:

    def __init__(self, id_number=-1, first="", last="", age=-1, phone=""):
        self.id = id_number
        self.first = first
        self.last = last
        self.age = age
        self.phone = phone
        self.connection = sqlite3.connect("workdb.db")
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM persons 
        WHERE id ={}
        """.format(id_number))

        result = self.cursor.fetchone()

        self.id_number = id_number
        self.first = result[1]
        self.last = result[2]
        self.age = result[3]
        self.phone = result[4]

    def insert_person(self, id_number, first, last, age, phone):
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ({},'{}','{}',{},'{}')
        """.format(id_number, first, last, age, phone))

        self.connection.commit()

    def search_data(self):
        choice = int(input("Select which kind of information you want to search for\n\
                           1.Search using unique ID\n\
                           2.Search using first name\n\
                           3.Search using last name\n\
                           4.Search using age\n\
                           5.Search using telephone number"))

        if choice == 1:
            print("You selected search method using id")
            user_id = int(input("Enter an id you want to search for"))
            self.cursor.execute("SELECT * FROM persons WHERE id = '%s'" % (user_id))
            raws = self.cursor.fetchone()
            print(raws)

        elif choice == 2:
            print("You selected search method using first name")
            name = input("Enter first name you want to search for")
            print(self.cursor.execute("SELECT * FROM persons WHERE name = '%s'" % (name)))
        elif choice == 3:
            print("You selected search method using last name")
            last_n = input("Enter last name you want to search for")
            print(self.cursor.execute("SELECT * FROM persons WHERE last_name = '%s'" % (last_n)))
        elif choice == 4:
            print("You selected search method using age")
            age = int(input("Enter an age you want to search for"))
            print(self.cursor.execute("SELECT * FROM persons WHERE age = '%s'" % (age)))
        elif choice == 5:
            print("You selected search method using phone number ")
            number = input("Enter a phone number you want to search for")
            print(self.cursor.execute("SELECT * FROM persons WHERE telephone_number = '%s'" % (number)))
        else:
            print("Following option does not exist")

    def print_person(self):
        number = int(input("Enter an id of a person you want to print out"))
        per = Person()
        per.load_person(number)
        print(per.id_number,
              per.first,
              per.last,
              per.age,
              per.phone)

    def input_person(self):
        id_n = int(input("Enter an id for a person"))
        first = input("Enter a name of a person")
        last = input("Enter a last name of a person")
        age = int(input("Enter an age of a person"))
        phone = input("Enter phone number of a person")
        return id_n, first, last, age, phone

    def start_prog(self):
        choice = int(input("Enter desired operation\n"
                           "1. Print out whole data base\n"
                           "2. Input into database\n"
                           "3.Search for a desired information in database\n"
                           "4. Find a person with id\n"
                           "5.To stop"))
        if choice == 1:
            connection = sqlite3.connect('workdb.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM persons")
            result = cursor.fetchall()
            print(result)
            Person.start_prog(self)
        elif choice == 2:
            a,b,c,d,e = Person.input_person(self)
            pl = Person()
            pl.insert_person(a,b,c,d,e)
            self.connection.commit()
            Person.start_prog(self)
        elif choice == 3:
            Person.search_data(self)
            Person.start_prog(self)
        elif choice == 4:
            Person.print_person(self)
            Person.start_prog(self)
        elif choice == 5:
            print("It was pleasure working with you ")
        else:
            print("Incorrect input")
            Person.start_prog(self)



