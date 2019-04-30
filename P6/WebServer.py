import http.server
import socketserver

PORT = 8009

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print(self.path)
        path_list = self.path.split('?')
        print(path_list)
        resource = path_list[0]

        if (len(path_list) == 1) and (resource == '/seq' or resource == '/'):
            file = open("MainPage.html", "r")
            contents = file.read()

        elif len(path_list) > 1 and (resource == '/seq'):
            print(self.path)
            parameters = path_list[1]
            print(parameters)
            functions = parameters.split('&')
            print(functions)
            seq = functions[0].split('=')
            bases = ["A", "C", "G", "T"]
            for x in seq[1]:
                if x != bases:
                    seq = False

            if seq == False:
                file = open("error2.html", "r")
                contents = file.read()

            elif ((functions[1] == 'base=A') or (functions[1] == 'base=T') or (functions[1] == 'base=C') or (functions[1] == 'base=G')) and (functions[2] == 'operation=count'):
                seq = functions[0].split('=')
                if functions[1] == 'base=A':
                    seq = functions[0].split('=')
                    result_A = 0
                    base = 'A'
                    for x in seq[1]:
                        if x == "A":
                            result_A += 1
                    count = result_A
                elif functions[1] == 'base=T':
                    base = 'T'
                    seq = functions[0].split('=')
                    result_T = 0
                    for x in seq[1]:
                        if x == "T":
                            result_T += 1
                    count = result_T
                elif functions[1] == 'base=C':
                    seq = functions[0].split('=')
                    result_C = 0
                    base = 'C'
                    for x in seq[1]:
                        if x == "C":
                            result_C += 1
                    count = result_C
                elif functions[1] == 'base=G':
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
                                     Count of {} bases:
                                     <l>{}</l>
                                     <br><br>
                                     <a href="/">HOME PAGE</a>
                                   </body>
                                 </html>""".format(base, count)

            if (functions[1] == 'chk=on')and((functions[2] == 'base=A') or (functions[2] == 'base=T') or (functions[2] == 'base=C') or (functions[2] == 'base=G')) and (functions[3] == 'operation=count'):
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

            elif ((functions[1] == 'base=A') or (functions[1] == 'base=T') or (functions[1] == 'base=C') or (functions[1] == 'base=G')) and (functions[2] == 'operation=perc'):
                seq = functions[0].split('=')
                length = len(seq[1])
                if functions[1] == 'base=A':
                    base = 'A'
                    result_A = 0
                    for x in seq[1]:
                        if x == "A":
                            result_A += 1
                    if length > 0:
                        perc = round(100.0 * result_A / length, 1)
                    else:
                        perc = 0
                elif functions[1] == 'base=T':
                    base = 'T'
                    result_T = 0
                    for x in seq[1]:
                        if x == "T":
                            result_T += 1
                    if length > 0:
                        perc = round(100.0 * result_T / length, 1)
                    else:
                        perc = 0
                elif functions[1] == 'base=C':
                    base = 'C'
                    result_C = 0
                    for x in seq[1]:
                        if x == "C":
                            result_C += 1
                    if length > 0:
                        perc = round(100.0 * result_C / length, 1)
                elif functions[1] == 'base=G':
                    base = 'G'
                    result_G = 0
                    for x in seq[1]:
                        if x == "G":
                            result_G += 1
                    if length > 0:
                        perc = round(100.0 * result_G / length, 1)
                    else:
                        perc = 0


                contents = """<!DOCTYPE html>
                                 <html lang="en">
                                   <head>
                                     <meta charset="utf-8">
                                     <title>Response</title>
                                   </head>
                                   <body style="background-color: #f8c471;">
                                     <h1>Response</h1>
                                     Percentage of {} base:
                                     <l>{}</l>
                                     <br><br>
                                     <a href="/">HOME PAGE</a>
                                   </body>
                                 </html>""".format(base, perc)

            elif (functions[1] == 'chk=on')and((functions[2] == 'base=A') or (functions[2] == 'base=T') or (functions[2] == 'base=C') or (functions[2] == 'base=G')) and (functions[3] == 'operation=perc'):
                seq = functions[0].split('=')
                length = len(seq[1])
                if functions[2] == 'base=A':
                    base = 'A'
                    result_A = 0
                    for x in seq[1]:
                        if x == "A":
                            result_A += 1
                    if length > 0:
                        perc = round(100.0 * result_A / length, 1)
                    else:
                        perc = 0
                elif functions[2] == 'base=T':
                    base = 'T'
                    result_T = 0
                    for x in seq[1]:
                        if x == "T":
                            result_T += 1
                    if length > 0:
                        perc = round(100.0 * result_T / length, 1)
                    else:
                        perc = 0
                elif functions[2] == 'base=C':
                    base = 'C'
                    result_C = 0
                    for x in seq[1]:
                        if x == "C":
                            result_C += 1
                    if length > 0:
                        perc = round(100.0 * result_C / length, 1)
                elif functions[2] == 'base=G':
                    base = 'G'
                    result_G = 0
                    for x in seq[1]:
                        if x == "G":
                            result_G += 1
                    if length > 0:
                        perc = round(100.0 * result_G / length, 1)
                    else:
                        perc = 0


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
                                     Percentage of {} base:
                                     <l>{}</l>
                                     <br><br>
                                     <a href="/">HOME PAGE</a>
                                   </body>
                                 </html>""".format(length, base, perc)

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
