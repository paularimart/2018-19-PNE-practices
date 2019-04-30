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

#-----------------------------------------------------------------------------------------------------------------------

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

print(per_A)
print(per_T)
print(per_C)
print(per_G)

#-----------------------------------------------------------------------------------------------------------------------

ENDPOINT_LIST_1 = '/overlap/region/human/'
Chromo = input('Type a chromosome: ')
Start = input('Type the start position: ')
End = input('Type the end position: ')
ENDPOINT_LIST_2 = '?feature=gene;feature=transcript;feature=cds;feature=exon;content-type=application/json'

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

for x in gene_list:
    type = x['feature_type']
    if type == 'gene':
        gene_name = x['external_name']
        print(gene_name)





