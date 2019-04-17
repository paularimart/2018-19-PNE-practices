import http.client
import json

HOSTNAME = 'rest.ensembl.org'

ENDPOINT_LIST_SPECIES = '/info/species?content-type=application/json'

ENDPOINT_KARYOTYPE_1 = '/info/assembly/'
ENDPOINT_KARYOTYPE_2 = '?content-type=application/json'
animal = input("Type a species to see its karyotype: ")

ENDPOINT_LENGTH_1 = '/info/assembly/'
ENDPOINT_LENGTH_2 = '?content-type=application/json'
animal_LENGTH = input("Type a species to see the lenght of its chromosomes: ")


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

for x in species['species']:
    print(x['name'])

#-----------------------------------------------------------------------------------------------------------------------
conn = http.client.HTTPConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT_KARYOTYPE_1 + animal + ENDPOINT_KARYOTYPE_2, None, headers)

r2 = conn.getresponse()

text_json = r2.read().decode("utf-8")
conn.close()

karyotype = json.loads(text_json)

for x in karyotype['karyotype']:
    print(x)

#-----------------------------------------------------------------------------------------------------------------------
conn = http.client.HTTPConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT_LENGTH_1 + animal + ENDPOINT_LENGTH_2, None, headers)

r3 = conn.getresponse()

text_json = r3.read().decode("utf-8")
conn.close()

chromosomes = json.loads(text_json)

number = len(chromosomes['karyotype'])
print(number)

for x in chromosomes['karyotype']:
    step1 = chromosomes['top_level_region']
    step2 = step1[x]
    step3 = step2['length']
    print(x, step2)






