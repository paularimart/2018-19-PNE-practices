import socket

PORT = 8082
IP = "212.128.253.70"
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

def complement(s):
    #dict_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
    comp_seq = ""
    for x in s:
        if x == "A":
            comp_seq += "T"
        elif x == "T":
            comp_seq += "A"
        elif x == "C":
            comp_seq += "G"
        elif x == "G":
            comp_seq += "C"
    return comp_seq

def reverse(s):
    rev_seq = s[::-1]
    return rev_seq


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
                len = length(message[0])
                print("The length of the sequence is: {}".format(len))
                cs.send(str.encode(msg))
            elif x == "complement":
                comp = complement(message[0])
                print("The complement of the sequence is: {}".format(comp))
                cs.send(str.encode(msg))
            elif x == "reverse":
                rev = reverse(message[0])
                print("The reverse of the sequence is: {}".format(rev))
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