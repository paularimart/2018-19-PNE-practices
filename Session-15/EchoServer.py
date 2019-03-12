#EXERCISE 1

import http.server
import socketserver
import termcolor

PORT = 8009

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

         request_line = self.requestline

         print("Request line:" + self.requestline)
         print("  Cmd: " + self.command)
         print("  Path: " + self.path)

         termcolor.cprint(self.requestline, 'green')

         if request_line.startswith("GET / ") or request_line.startswith("GET /echo"):
             file = open("Form_ex1.html", "r")
             contents = file.read()
         else:
             file = open("Error_ex1.html", "r")
             contents = file.read()

         self.send_response(200)

         self.send_header('Content-Type', 'text/html')
         self.send_header('Content-Length', len(str.encode(contents)))
         self.end_headers()

         #--Sending the body of the response message
         self.wfile.write(str.encode(contents))


# -- Main program
with socketserver.TCPServer(("212.128.253.67", PORT), TestHandler) as httpd:
    print("Serving at port: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
