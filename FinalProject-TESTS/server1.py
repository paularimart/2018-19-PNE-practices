import http.server
import socketserver
import termcolor
import http.client
import json

PORT = 8005

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        print(self.path)
        path_list = self.path.split('?')
        print(path_list)
        resource = path_list[0]
        print(resource)
        if resource == '/':
            f = open("form1.html", 'r')
            contents = f.read()

        elif resource == '/myserver':
            print(self.path)
            resource_2 = self.path.split('?')
            print(resource_2)
            options = resource_2[1]
            print(options)
            param_list = options.split('&')
            print(param_list)

            if param_list[0] == 'list_species=on':
                HOSTNAME = 'rest.ensembl.org'
                ENDPOINT_LIST_SPECIES = '/info/species?content-type=application/json'
                METHOD = "GET"

                headers = {'User-Agent': 'http-client'}

                conn = http.client.HTTPSConnection(HOSTNAME)

                conn.request(METHOD, ENDPOINT_LIST_SPECIES, None, headers)

                r1 = conn.getresponse()

                print()
                print("Response received: ", end='')
                print(r1.status, r1.reason)
                print()

                text_json = r1.read().decode("utf-8")
                conn.close()

                species = json.loads(text_json)

                for x in species['species']:
                    list = x['name']
                    print(list)
                    contents = """<!DOCTYPE html>
                                     <html lang="en">
                                       <head>
                                         <meta charset="utf-8">
                                         <title>List Species</title>
                                       </head>
                                       <body style="background-color: #7cc3f3;">
                                         <h1>List of species</h1>
                                         <p>{}<p>
                                         <a href="/">HOME PAGE</a>
                                       </body>
                                     </html>""".format(list)

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
