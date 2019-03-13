#EXERCISE 1

import http.server
import socketserver
import termcolor

PORT = 8007

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print(self.path)
        path_list = self.path.split('?')
        print(path_list)
        resource = path_list[0]
        if resource == '/':
            file = open("Form_ex1.html", "r")
            contents = file.read()
        elif resource == '/echo':
            msg = self.path[10:]
            file_2 = open("Response_form.html", "w")
            contents_1 = """<!DOCTYPE html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Echo Page</title>
                      </head>
                      <body style="background-color: #D8CEF6;">
                        <h1>Echo of the received message</h1>
                        <p>{}<p>
                        <a href="/">HOME PAGE</a>
                      </body>
                    </html>""".format(msg)

            file_2.write(contents_1)
            file_2.close()
            file = open("Response_form.html", "r")
            contents = file.read()
        else:
            file = open("Error_ex1.html", "r")
            contents = file.read()

        termcolor.cprint(self.requestline, 'green')

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        #--Sending the body of the response message
        self.wfile.write(str.encode(contents))


# -- Main program
with socketserver.TCPServer(("212.128.253.68", PORT), TestHandler) as httpd:
    print("Serving at port: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
