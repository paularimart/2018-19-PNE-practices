import http.server
import socketserver
import termcolor

PORT = 8009

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

         termcolor.cprint(self.requestline, 'green')

         print(self.path)
         path_list = self.path.split('?')
         print(path_list)
         resource = path_list[0]
         #resource_2 = resource.split['&']
         if resource == '/':
            f = open("form1.html", 'r')
            contents = f.read()
         else:
             file = open("error1.html", "r")
             contents = file.read()

         self.send_response(200)

         self.send_header('Content-Type', 'text/html')
         self.send_header('Content-Length', len(str.encode(contents)))
         self.end_headers()

         self.wfile.write(str.encode(contents))


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at port: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
