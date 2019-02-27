import socket

PORT = 8081
IP = "212.128.253.67"
#Maximum number of clients that can connect to this server
MAX_OPEN_REQUEST = 5

def check(s):
    for x in s:
        if x != "A" and x != "T" and x != "C" and x != "G":
            seq = "bad"
            break
        else:
            seq = "good"
    if seq == "bad":
        print("ERROR")
    else:
        print("OK")

def length(s):
    return len(s)

def process_client(cs):

    #ECHO SERVER
    #Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    message = msg.split("\n")

    print("Message from the client: {}". format(message))

    if message[0] == "":
        print("ALIVE")
    else:
        check(message[0])
        for x in message:
            if x == "len":
                x = length(message[0])
                print("The length of the sequence is: {}".format(x))
                cs.send(str.encode(msg))

    cs.close()

#Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

#To listen to the client's requests
serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}". format(serversocket))

while True:

    print("Waiting for connections at: {}, {}". format(IP, PORT))
    (clientsocket, adress) = serversocket.accept()

    #-- Process the client request
    print("Attending client: {}". format(adress))

    process_client(clientsocket)


    #-- Close the socket
    clientsocket.close()