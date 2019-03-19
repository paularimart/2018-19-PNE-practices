import json
import termcolor

f = open("person-ex1.json", 'r')

person = json.load(f)

print()

for i,num in enumerate(person['Person_1']):
    termcolor.cprint("Name: ", 'cyan', end='')
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("Age: ", 'cyan', end='')
    print(person['Age'])

    phoneNumbers = person['PhoneNumber']
    termcolor.cprint("Phone numbers: ", 'cyan', end='')
    print(len(phoneNumbers))
    for i,num in enumerate(person['PhoneNumber']):
        termcolor.cprint(" Phone number {}: ".format(i), 'yellow')
        termcolor.cprint("  Type: ", 'blue', end='')
        print(num['type'])
        termcolor.cprint("  Number: ", 'blue', end='')
        print(num['number'])