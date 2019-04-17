import http.server
import socketserver
import http.client
import json

PORT = 8005

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print(self.requestline)

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

                conn = http.client.HTTPConnection(HOSTNAME)

                conn.request(METHOD, ENDPOINT_LIST_SPECIES, None, headers)

                r1 = conn.getresponse()

                print()
                print("Response received: ", end='')
                print(r1.status, r1.reason)
                print()

                text_json = r1.read().decode("utf-8")
                conn.close()

                species = json.loads(text_json)

                list_species = ''
                for x in species['species']:
                    list = x['name']
                    print(list)
                    list_species = list_species + '<li>{}</li>'.format(list)
                    contents = """<!DOCTYPE html>
                                     <html lang="en">
                                       <head>
                                         <meta charset="utf-8">
                                         <title>List Species</title>
                                       </head>
                                       <body style="background-color: #7cc3f3;">
                                         <h1>List of species</h1>
                                         <l>{}</l>
                                         <a href="/">HOME PAGE</a>
                                       </body>
                                     </html>""".format(list_species)

            elif param_list[1] == 'karyotype=on':
                HOSTNAME = 'rest.ensembl.org'
                ENDPOINT_KARYOTYPE_1 = '/info/assembly/'
                ENDPOINT_KARYOTYPE_2 = '?content-type=application/json'
                specie_k = param_list[2].split('=')
                animal = specie_k[1]
                print(animal)
                METHOD = "GET"

                headers = {'User-Agent': 'http-client'}

                conn = http.client.HTTPConnection(HOSTNAME)

                conn.request(METHOD, ENDPOINT_KARYOTYPE_1 + animal + ENDPOINT_KARYOTYPE_2, None, headers)

                r2 = conn.getresponse()

                text_json = r2.read().decode("utf-8")
                conn.close()

                karyotype = json.loads(text_json)

                chromosomes = ''
                for x in karyotype['karyotype']:
                    name = x
                    print(name)
                    chromosomes = chromosomes + '<li>{}</li>'.format(name)
                    contents = """<!DOCTYPE html>
                                     <html lang="en">
                                       <head>
                                         <meta charset="utf-8">
                                         <title>List Species</title>
                                       </head>
                                       <body style="background-color: #7cc3f3;">
                                         <h1>Karyotype</h1>
                                         <l>{}</l>
                                         <a href="/">HOME PAGE</a>
                                       </body>
                                     </html>""".format(chromosomes)


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
