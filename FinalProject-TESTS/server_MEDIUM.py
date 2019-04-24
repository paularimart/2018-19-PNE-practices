import http.server
import socketserver
import http.client
import json

PORT = 8001

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

        elif resource == '/listSpecies':
            if len(path_list) == 1:
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
                                                     <br><br>
                                                     <a href="/">HOME PAGE</a>
                                                   </body>
                                                 </html>""".format(list_species)
            elif len(path_list) > 1:
                request = path_list[1].split('=')
                limit = request[1]
                print(limit)

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
                y = 0
                for x in species['species']:
                    y += 1
                    if y <= int(limit):
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
                                             <br><br>
                                             <a href="/">HOME PAGE</a>
                                           </body>
                                         </html>""".format(list_species)

        elif resource == '/karyotype':
        #elif param_list[1] == 'karyotype=on':
            HOSTNAME = 'rest.ensembl.org'
            ENDPOINT_KARYOTYPE_1 = '/info/assembly/'
            ENDPOINT_KARYOTYPE_2 = '?content-type=application/json'
            print(self.path)
            resource_2 = self.path.split('?')
            print(resource_2)
            options = resource_2[1]
            print(options)
            param_list = options.split('&')
            print(param_list)
            specie_k = param_list[0].split('=')
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
                                     <title>Karyotype</title>
                                   </head>
                                   <body style="background-color: #7cc3f3;">
                                     <h1>Karyotype</h1>
                                     <l>{}</l>
                                     <br><br>
                                     <a href="/">HOME PAGE</a>
                                   </body>
                                 </html>""".format(chromosomes)

        elif resource == '/chromosomeLength':
            HOSTNAME = 'rest.ensembl.org'
            ENDPOINT_LENGTH_1 = '/info/assembly/'
            ENDPOINT_LENGTH_2 = '?content-type=application/json'
            print(self.path)
            resource_2 = self.path.split('?')
            print(resource_2)
            options = resource_2[1]
            print(options)
            param_list = options.split('&')
            print(param_list)
            specie_k = param_list[0].split('=')
            animal = specie_k[1]
            print(animal)
            chromo = param_list[1].split('=')
            num_chromo = chromo[1]
            print(num_chromo)
            METHOD = "GET"

            headers = {'User-Agent': 'http-client'}

            conn = http.client.HTTPConnection(HOSTNAME)

            conn.request(METHOD, ENDPOINT_LENGTH_1 + animal + ENDPOINT_LENGTH_2, None, headers)

            r3 = conn.getresponse()

            text_json = r3.read().decode("utf-8")
            conn.close()

            chromosomes = json.loads(text_json)

            for x in chromosomes['karyotype']:
                step1 = chromosomes['top_level_region']
                for y in step1:
                    step2 = y['name']
                    if step2 == num_chromo:
                        step3 = y['length']
                        print(num_chromo, step3)
                        contents = """<!DOCTYPE html>
                                         <html lang="en">
                                           <head>
                                             <meta charset="utf-8">
                                             <title>Chromosome length</title>
                                           </head>
                                           <body style="background-color: #7cc3f3;">
                                             <h1>Chromosome length</h1>
                                             <l>{}: {}</l>
                                             <br><br>
                                             <a href="/">HOME PAGE</a>
                                           </body>
                                         </html>""".format(num_chromo, step3)

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
