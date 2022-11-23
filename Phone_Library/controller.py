import export_data as ed
import import_data as id
import print_data as pd
import search_data as sd
def welcomig():
    print("Hello, and welcome to phone dictionary")

def input_data():
    first_name = input("Enter first name")
    last_name = input("Enter last name")
    phone_number = input("Enter telephone number")
    notes = input("Enter a note to the contact you are recording")
    return [first_name, last_name,phone_number,notes]


def choice_sep():
    sep = input("Enter a separator: ")
    if sep == "":
        sep = None
    return sep

def choice():
    print("What do you need to do?:\n\
    1 - input;\n\
    2 - export;\n\
    3 - search for.")
    ch = input("Enter a number: ")
    if ch == '1':
        sep = choice_sep()
        id.import_data(input_data(), sep)
    elif ch == '2':
        data = ed.export_data()
        pd.print_data(data)
    else:
        word = input("Enter data for searching process: ")
        data = ed.export_data()
        item = sd.search_data(word, data)
        if item != None:
            print("Name".center(20), "Last name".center(20), "Telephone".center(15), "Note".center(30))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            print("Data is not found")