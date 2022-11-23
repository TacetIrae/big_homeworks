
def print_data(data):
    if len(data) > 0:
        print("First Name".center(20), "Last Name".center(20), "Telephone".center(15), "Note".center(30))
        print("-"*85)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
    else:
        print("Phone dictionary is empty")
