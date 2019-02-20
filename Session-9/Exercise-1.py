import socket
import termcolor

PORT = 8083
IP = "212.128.253.74"
#Maximum number of clients that can connect to this server
MAX_OPEN_REQUEST = 5

def process_client(cs):

    #ECHO SERVER
    #Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    termcolor.cprint(msg, 'magenta')
    # Sending the message back to the client
    cs.send(str.encode(msg))

    cs.close()

#Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

#To listen to the client's requests
serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}". format(serversocket))

print("Waiting for connections at: {}, {}". format(IP, PORT))
(clientsocket, adress) = serversocket.accept()

#-- Process the client request
print("Attending client: {}". format(adress))

#msg = clientsocket.recv(2048).decode("utf-8")

if msg == "EXIT":
    # -- Close the socket
    clientsocket.close()
else:
    process_client(clientsocket)




