import socket

PORT = 8087
IP = "212.128.253.74"
#Maximum number of clients that can connect to this server
MAX_OPEN_REQUEST = 5

def check(s):
    if s == "":
        print("ALIVE")
    else:
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

    #print("Message from the client: {}". format(msg))
    # Sending the message back to the client
    #cs.send(str.encode(msg))

    if msg == "len":
        x = length(msg)
        print("The length of the sequence is: {}". format(x))
        cs.send(str.encode(msg))
    else:
        check(msg)

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