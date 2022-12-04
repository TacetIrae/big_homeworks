import import_Info as im_inf
import export_info as exp_inf
import print_list as pl
import search_info as sea_inf


def welcome():
    print("Welcome to the data-base")



def splitter():
    sep = input("Enter desired separator")
    return sep



def choice():
    print("1 - Input new data;\n\
     2 - Search for existing information;\n\
     3 - Export data;\n\
     4 - Import a lot of data")
    choice = input("Enter your choice")
    if choice == '1':
        im_inf.Import_data(input_data(),splitter())
    elif choice == '2':
        word = input('Enter desired information to be searched')
        data = exp_inf.export_data()
        desired_info = sea_inf.search_data(word,data)
    elif choice == '3':

    elif choice == '4':
        im_inf.import_set_data(input_list_name(),input_list_surname(),input_list_birth(),input_list_grade(),splitter())




    else: print ("Incorrect input")



def input_data():
    name = input("Enter a first name of a student")
    surname = input("Enter a surname of a student")
    age = input("Enter data of birth of a student ")
    grade = input("Enter at which grade of university student currently is")
    return [name, surname, age, grade]


def input_list_name():
    names = input("Enter names\n\
    Enter a list of data separating each unit  with ','")
    return names


def input_list_surname():
    surnames = input ("Enter Surnames\n\
    Enter a list of data separating each unit with ','")
    return surnames


def input_list_birth ():
    birth = input("Enter birth date\n\
    Enter a list of data separating each unit with ','")
    return birth


def input_list_grade():
    grade = input("Enter a grades of students\n\
        Enter a list of data separating each unit with ','")

