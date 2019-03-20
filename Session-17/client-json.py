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

print("Total people in the database: ", len(person))

for object in person:
    termcolor.cprint("Name: ", 'cyan', end='')
    print(object['Firstname'], object['Lastname'])
    termcolor.cprint("Age: ", 'cyan', end='')
    print(object['Age'])
    phoneNumbers = object['PhoneNumber']
    termcolor.cprint("Phone numbers: ", 'cyan', end='')
    print(len(phoneNumbers))
    for i,num in enumerate(object['PhoneNumber']):
        termcolor.cprint(" Phone number {}: ".format(i), 'yellow')
        termcolor.cprint("  Type: ", 'blue', end='')
        print(num['type'])
        termcolor.cprint("  Number: ", 'blue', end='')
        print(num['number'])
    print()