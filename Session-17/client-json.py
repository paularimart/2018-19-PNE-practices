# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import termcolor
import json

PORT = 8001
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

print("CONTENT: ")

# -- Print the received data
print(data1)

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

print("CONTENT: ")

# Print the information in the object
print()
termcolor.cprint("Name: ", 'cyan', end="")
print(person['Firstname'], person['Lastname'])

termcolor.cprint("Age: ", 'cyan', end="")
print(person['Age'])

# Get the phoneNumber list
phoneNumbers = person['PhoneNumber']

# Print the number of elements int the list
termcolor.cprint("Phone numbers: ", 'cyan', end='')
print(len(phoneNumbers))

# Print all the numbers
for i, num in enumerate(phoneNumbers):
    termcolor.cprint("  Phone {}:".format(i), 'blue')

    # The element num contains 2 fields: number and type
    termcolor.cprint("    Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("    Number: ", 'red', end='')
    print(num['number'])

print()
termcolor.cprint("Name: ", 'cyan', end="")
print(person['Firstname_2'], person['Lastname_2'])

termcolor.cprint("Age: ", 'cyan', end="")
print(person['Age_2'])

# Get the phoneNumber list
phoneNumbers = person['PhoneNumber_2']

# Print the number of elements int the list
termcolor.cprint("Phone numbers: ", 'cyan', end='')
print(len(phoneNumbers))

# Print all the numbers
for i, num in enumerate(phoneNumbers):
    termcolor.cprint("  Phone {}:".format(i), 'blue')

    # The element num contains 2 fields: number and type
    termcolor.cprint("    Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("    Number: ", 'red', end='')
    print(num['number'])

print()
termcolor.cprint("Name: ", 'cyan', end="")
print(person['Firstname_3'], person['Lastname_3'])

termcolor.cprint("Age: ", 'cyan', end="")
print(person['Age_3'])

# Get the phoneNumber list
phoneNumbers = person['PhoneNumber_3']

# Print the number of elements int the list
termcolor.cprint("Phone numbers: ", 'cyan', end='')
print(len(phoneNumbers))

# Print all the numbers
for i, num in enumerate(phoneNumbers):
    termcolor.cprint("  Phone {}:".format(i), 'blue')

    # The element num contains 2 fields: number and type
    termcolor.cprint("    Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("    Number: ", 'red', end='')
    print(num['number'])