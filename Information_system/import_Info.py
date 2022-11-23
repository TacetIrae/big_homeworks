
def Import_data (data, sep):
    with open("Data_base.cvs", 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")

def import_set_data (name, surname, birth,grade,sep):
    names = []
    surnames = []
    births = []
    grades = []
    names = name.split(',')
    surnames = surname.split(',')
    births = birth.split(',')
    grades = grade.split(',')
    with open("Data_base.cvs", "a+") as file:
    for i in len(names):
        data = names[i],surnames[i],births[i],grades[i]
        file.write(sep.join(data))


