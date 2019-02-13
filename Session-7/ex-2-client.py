import socket

# SERVER IP, PORT
IP = "212.128.253.65"
PORT = 8080

# First, create the socket
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send data. No strings can be send, only bytes
    # It necesary to encode the string into bytes
    message = input("Type your message: ")
    s.send(str.encode(message))

    # Receive data from the server
    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:\n")
    print(msg)