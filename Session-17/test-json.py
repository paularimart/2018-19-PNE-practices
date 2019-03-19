import json
import termcolor

f = open("person.json", 'r')

person = json.load(f)

print()

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

print()

termcolor.cprint("Name: ", 'cyan', end='')
print(person['Firstname_2'], person['Lastname_2'])

termcolor.cprint("Age: ", 'cyan', end='')
print(person['Age_2'])

phoneNumbers = person['PhoneNumber']
termcolor.cprint("Phone numbers: ", 'cyan', end='')
print(len(phoneNumbers))
for i,num in enumerate(person['PhoneNumber_2']):
    termcolor.cprint(" Phone number {}: ".format(i), 'yellow')
    termcolor.cprint("  Type: ", 'blue', end='')
    print(num['type'])
    termcolor.cprint("  Number: ", 'blue', end='')
    print(num['number'])

print()

termcolor.cprint("Name: ", 'cyan', end='')
print(person['Firstname_3'], person['Lastname_3'])

termcolor.cprint("Age: ", 'cyan', end='')
print(person['Age_3'])

phoneNumbers = person['PhoneNumber']
termcolor.cprint("Phone numbers: ", 'cyan', end='')
print(len(phoneNumbers))
for i,num in enumerate(person['PhoneNumber_3']):
    termcolor.cprint(" Phone number {}: ".format(i), 'yellow')
    termcolor.cprint("  Type: ", 'blue', end='')
    print(num['type'])
    termcolor.cprint("  Number: ", 'blue', end='')
    print(num['number'])






