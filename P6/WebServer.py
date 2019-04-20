import http.server
import socketserver
from seqs import Seq

PORT = 8009

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print(self.path)
        path_list = self.path.split('?')
        print(path_list)
        resource = path_list[0]
        if resource == '/':
            file = open("MainPage.html", "r")
            contents = file.read()

        elif resource == '/form':
            print(self.path)
            parameters = path_list[1]
            print(parameters)
            functions = parameters.split('&')
            print(functions)
            #seq = functions[0].split('=')
            #bases = ["A", "C", "G", "T"]
            #for x in seq:
                #if x != bases:
                    #file = open("Error.html", "r")
                    #contents = file.read()

            if (functions[1] == 'chk=on')and(functions[2] == 'base=A') or (functions[2] == 'base=T') or (functions[2] == 'base=C') or (functions[2] == 'base=G') and (functions[3] == 'operation=count'):
                seq = functions[0].split('=')
                length = len(seq[1])
                if functions[2] == 'base=A':
                    seq = functions[0].split('=')
                    result_A = 0
                    base = 'A'
                    for x in seq[1]:
                        if x == "A":
                            result_A += 1
                    count = result_A
                elif functions[2] == 'base=T':
                    base = 'T'
                    seq = functions[0].split('=')
                    result_T = 0
                    for x in seq[1]:
                        if x == "T":
                            result_T += 1
                    count = result_T
                elif functions[2] == 'base=C':
                    seq = functions[0].split('=')
                    result_C = 0
                    base = 'C'
                    for x in seq[1]:
                        if x == "C":
                            result_C += 1
                    count = result_C
                elif functions[2] == 'base=G':
                    seq = functions[0].split('=')
                    result_G = 0
                    base = 'G'
                    for x in seq[1]:
                        if x == "G":
                            result_G += 1
                    count = result_G

                contents = """<!DOCTYPE html>
                                 <html lang="en">
                                   <head>
                                     <meta charset="utf-8">
                                     <title>Response</title>
                                   </head>
                                   <body style="background-color: #f8c471;">
                                     <h1>Response</h1>
                                     Length:
                                     <l>{}</l>
                                     <br>
                                     Count of {} bases:
                                     <l>{}</l>
                                     <br><br>
                                     <a href="/">HOME PAGE</a>
                                   </body>
                                 </html>""".format(length, base, count)


        else:
            file = open("Error.html", "r")
            contents = file.read()

        #print(self.requestline)

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # --Sending the body of the response message
        self.wfile.write(str.encode(contents))

# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at port: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
