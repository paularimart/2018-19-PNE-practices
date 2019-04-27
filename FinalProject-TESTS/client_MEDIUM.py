import http.client
import json

HOSTNAME = 'rest.ensembl.org'

ENDPOINT_1 = '/xrefs/symbol/homo_sapiens/'
human_gene = input('Type a gene: ')
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

#-----------------------------------------------------------------------------------------------------------------------



