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

        elif resource == '/geneSeq':
            HOSTNAME = 'rest.ensembl.org'
            ENDPOINT_1 = '/xrefs/symbol/homo_sapiens/'
            name = path_list[1]
            genes = name.split('=')
            human_gene = genes[1]
            print(human_gene)
            ENDPOINT_2 = '?content-type=application/json'
            METHOD = 'GET'

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPConnection(HOSTNAME)
            conn.request(METHOD, ENDPOINT_1 + human_gene + ENDPOINT_2, None, headers)

            r1 = conn.getresponse()
            print()
            print("Response received: ", end='')
            print(r1.status, r1.reason)
            print()
            text_json = r1.read().decode("utf-8")
            conn.close()

            gene = json.loads(text_json)

            step_01 = gene[0]
            ensembl_id = step_01['id']

            print(ensembl_id)

            ENDPOINT_SEQ_1 = '/sequence/id/'
            ENDPOINT_SEQ_2 = '?content-type=application/json'

            headers = {'User-Agent': 'http-client'}

            conn = http.client.HTTPConnection(HOSTNAME)

            conn.request(METHOD, ENDPOINT_SEQ_1 + ensembl_id + ENDPOINT_SEQ_2, None, headers)

            r2 = conn.getresponse()

            print()
            print("Response received: ", end='')
            print(r2.status, r2.reason)
            print()

            text_json = r2.read().decode("utf-8")
            conn.close()

            seq = json.loads(text_json)
            gene_seq = seq['seq']

            print(gene_seq)

            contents = """<!DOCTYPE html>
                             <html lang="en">
                               <head>
                                 <meta charset="utf-8">
                                 <title>Gene seq</title>
                               </head>
                               <body style="background-color: #7cc3f3;">
                                 <h1>Gene Sequence</h1>
                                 <l>{}: {}</l>
                                 <br><br>
                                 <a href="/">HOME PAGE</a>
                               </body>
                             </html>""".format(human_gene, gene_seq)

        elif resource == '/geneInfo':
            HOSTNAME = 'rest.ensembl.org'
            ENDPOINT_1 = '/xrefs/symbol/homo_sapiens/'
            name = path_list[1]
            genes = name.split('=')
            human_gene = genes[1]
            print(human_gene)
            ENDPOINT_2 = '?content-type=application/json'
            METHOD = 'GET'

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPConnection(HOSTNAME)
            conn.request(METHOD, ENDPOINT_1 + human_gene + ENDPOINT_2, None, headers)

            r1 = conn.getresponse()
            print()
            print("Response received: ", end='')
            print(r1.status, r1.reason)
            print()
            text_json = r1.read().decode("utf-8")
            conn.close()

            gene = json.loads(text_json)

            step_01 = gene[0]
            ensembl_id = step_01['id']

            print(ensembl_id)

            ENDPOINT_INFO_1 = '/overlap/id/'
            ENDPOINT_INFO_2 = '?content-type=application/json;feature=gene'

            headers = {'User-Agent': 'http-client'}

            conn = http.client.HTTPConnection(HOSTNAME)

            conn.request(METHOD, ENDPOINT_INFO_1 + ensembl_id + ENDPOINT_INFO_2, None, headers)

            r3 = conn.getresponse()

            print()
            print("Response received: ", end='')
            print(r3.status, r3.reason)
            print()

            text_json = r3.read().decode("utf-8")
            conn.close()

            info = json.loads(text_json)

            Information = info[0]

            start = Information['start']
            end = Information['end']
            length = int(end) - int(start) + 1
            ID = Information['id']
            chromosome = Information['seq_region_name']

            print(start)
            print(end)
            print(length)
            print(ID)
            print(chromosome)

            contents = """<!DOCTYPE html>
                             <html lang="en">
                               <head>
                                 <meta charset="utf-8">
                                 <title>Gene Info</title>
                               </head>
                               <body style="background-color: #7cc3f3;">
                                 <h1>Human gene information</h1>
                                 <p>{} <p>
                                 <p>start:{}<p>
                                 <p>end: {}<p> 
                                 <p>length: {}<p> 
                                 <p>ID: {}<p>
                                 <p>chromosome: {}<p>
                                 <br><br>
                                 <a href="/">HOME PAGE</a>
                               </body>
                             </html>""".format(human_gene, start, end, length, ID, chromosome)

        elif resource == '/geneCalc':
            HOSTNAME = 'rest.ensembl.org'
            ENDPOINT_1 = '/xrefs/symbol/homo_sapiens/'
            name = path_list[1]
            genes = name.split('=')
            human_gene = genes[1]
            print(human_gene)
            ENDPOINT_2 = '?content-type=application/json'
            METHOD = 'GET'

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPConnection(HOSTNAME)
            conn.request(METHOD, ENDPOINT_1 + human_gene + ENDPOINT_2, None, headers)

            r1 = conn.getresponse()
            print()
            print("Response received: ", end='')
            print(r1.status, r1.reason)
            print()
            text_json = r1.read().decode("utf-8")
            conn.close()

            gene = json.loads(text_json)

            step_01 = gene[0]
            ensembl_id = step_01['id']

            ENDPOINT_SEQ_1 = '/sequence/id/'
            ENDPOINT_SEQ_2 = '?content-type=application/json'

            headers = {'User-Agent': 'http-client'}

            conn = http.client.HTTPConnection(HOSTNAME)

            conn.request(METHOD, ENDPOINT_SEQ_1 + ensembl_id + ENDPOINT_SEQ_2, None, headers)

            r2 = conn.getresponse()

            print()
            print("Response received: ", end='')
            print(r2.status, r2.reason)
            print()

            text_json = r2.read().decode("utf-8")
            conn.close()

            seq = json.loads(text_json)
            gene_seq = seq['seq']

            gene_length = len(gene_seq)

            result_A = 0
            result_T = 0
            result_C = 0
            result_G = 0

            for x in gene_seq:
                if x == "A":
                    result_A += 1
                elif x == "T":
                    result_T += 1
                elif x == "C":
                    result_C += 1
                else:
                    result_G += 1

            if gene_length > 0:
                per_A = round(100.0 * result_A / gene_length, 1)
            else:
                per_A = 0

            if gene_length > 0:
                per_T = round(100.0 * result_T / gene_length, 1)
            else:
                per_T = 0

            if gene_length > 0:
                per_C = round(100.0 * result_C / gene_length, 1)
            else:
                per_C = 0

            if gene_length > 0:
                per_G = round(100.0 * result_G / gene_length, 1)
            else:
                per_G = 0

            contents = """<!DOCTYPE html>
                             <html lang="en">
                               <head>
                                 <meta charset="utf-8">
                                 <title>Gene Calc</title>
                               </head>
                               <body style="background-color: #7cc3f3;">
                                 <h1>Human gene calculations - Percentage of each base</h1>
                                 <p>{} <p>
                                 <p>Length: {}<p>
                                 <p>Percentage A: {}<p> 
                                 <p>Percentage T: {}<p> 
                                 <p>Percentage C: {}<p>
                                 <p>Percentage G: {}<p>
                                 <br><br>
                                 <a href="/">HOME PAGE</a>
                               </body>
                             </html>""".format(human_gene, gene_length, per_A, per_T, per_C, per_G)

        elif resource == '/geneList':
            print(path_list)
            parameters = path_list[1]
            param = parameters.split('&')
            param_1 = param[0]
            param_1_chromo = param_1.split('=')
            Chromo = param_1_chromo[1]
            param_2 = param[1]
            param_2_start = param_2.split('=')
            Start = param_2_start[1]
            param_3 = param[2]
            param_3_end = param_3.split('=')
            End = param_3_end[1]
            print(Chromo)
            print(Start)
            print(End)

            HOSTNAME = 'rest.ensembl.org'
            ENDPOINT_LIST_1 = '/overlap/region/human/'
            ENDPOINT_LIST_2 = '?feature=gene;feature=transcript;feature=cds;feature=exon;content-type=application/json'
            METHOD = 'GET'

            headers = {'User-Agent': 'http-client'}

            conn = http.client.HTTPConnection(HOSTNAME)

            conn.request(METHOD, ENDPOINT_LIST_1 + Chromo + ':' + Start + '-' + End + ENDPOINT_LIST_2, None, headers)

            r4 = conn.getresponse()

            print()
            print("Response received: ", end='')
            print(r4.status, r4.reason)
            print()

            text_json = r4.read().decode("utf-8")
            conn.close()

            gene_list = json.loads(text_json)

            list_genes = ''
            for x in gene_list:
                type = x['feature_type']
                if type == 'gene':
                    gene_name = x['external_name']
                    print(gene_name)
                    list_genes = list_genes + '<li>{}</li>'.format(gene_name)
                    contents ="""<!DOCTYPE html>
                                     <html lang="en">
                                       <head>
                                         <meta charset="utf-8">
                                         <title>Gene list</title>
                                       </head>
                                       <body style="background-color: #7cc3f3;">
                                         <h1>List of genes</h1>
                                         <l>{}</l>
                                         <br><br>
                                         <a href="/">HOME PAGE</a>
                                       </body>
                                     </html>""".format(list_genes)

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
