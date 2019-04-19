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

            if functions[1] == 'chk=on':
                seq = functions[0].split('=')
                length = len(seq[1])
                print(length)
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
                                     <br><br>
                                     <a href="/">HOME PAGE</a>
                                   </body>
                                 </html>""".format(length)

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
