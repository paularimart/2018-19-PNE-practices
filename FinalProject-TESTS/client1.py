import http.client
import json

HOSTNAME = 'rest.ensembl.org'
ENDPOINT_LIST_SPECIES = '/info/species?content-type=application/json'
ENDPOINT_KARYOTYPE = '/info/assembly/equus_caballus?content-type=application/json'
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
    print(x['name'])

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT_KARYOTYPE, None, headers)

r2 = conn.getresponse()

text_json = r2.read().decode("utf-8")
conn.close()

karyotype = json.loads(text_json)

for x in karyotype['karyotype']:
    print(x)