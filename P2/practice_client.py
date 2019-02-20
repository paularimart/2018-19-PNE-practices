
import socket

# SERVER IP, PORT
IP = "212.128.253.74"
PORT = 8082

# First, create the socket
while True:
    class Seq:
        """A class for representing sequences"""

        def __init__(self, strmessage):
            print("New sequence created!")

            self.strmessage = strmessage

        def rev_comp(self):
            # dict_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
            comp_seq = ""
            for x in self.strmessage:
                if x == "A":
                    comp_seq += "T"
                elif x == "T":
                    comp_seq += "A"
                elif x == "C":
                    comp_seq += "G"
                elif x == "G":
                    comp_seq += "C"

            rev_seq = comp_seq[::-1]
            return rev_seq


    class Message(Seq):
        pass


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send data. No strings can be send, only bytes
    # It necesary to encode the string into bytes
    message = Message(input("Type your message: "))
    seq = message.strmessage

    seq_c = message.rev_comp()

    s.send(str.encode(seq_c))

    # Receive data from the server
    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:\n")
    print(msg)
