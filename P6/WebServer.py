import http.server
import socketserver
import termcolor
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
        else:
            file = open("Error.html", "r")
            contents = file.read()

        termcolor.cprint(self.requestline, 'green')

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # --Sending the body of the response message
        self.wfile.write(str.encode(contents))

        termcolor.cprint('New requestline', 'red')
        list_1 = path_list[1].split('msg=')
        print(list_1)
        list_2 = list_1[1].split('&')
        print(list_2)

# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at port: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
