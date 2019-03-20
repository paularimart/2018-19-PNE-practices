import json
import termcolor

f = open("person-ex1.json", 'r')

person = json.load(f)

print()

print("Total people in the database: ", len(person))

for object in person:
    termcolor.cprint("Name: ", 'cyan', end='')
    print(object['Firstname'], object['Lastname'])
    termcolor.cprint("Age: ", 'cyan', end='')
    print(object['Age'])
    phoneNumbers = object['PhoneNumber']
    termcolor.cprint("Phone numbers: ", 'cyan', end='')
    print(len(phoneNumbers))
    for i, num in enumerate(object['PhoneNumber']):
        termcolor.cprint(" Phone number {}: ".format(i), 'yellow')
        termcolor.cprint("  Type: ", 'blue', end='')
        print(num['type'])
        termcolor.cprint("  Number: ", 'blue', end='')
        print(num['number'])
    print()
