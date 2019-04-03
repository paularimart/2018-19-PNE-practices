import http.client
import json

HOSTNAME = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/ENSG00000165879'
METHOD = "GET"
PARAMETER = '?content-type=application/json'

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + PARAMETER, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

info = json.loads(text_json)
seq = info['seq']

print("Number of bases in the FRAT1 gene: ", len(seq))

num_T = 0
num_A = 0
num_C = 0
num_G = 0

for base in seq:
    if base == 'T':
        num_T += 1
    elif base == 'A':
        num_A += 1
    elif base == 'C':
        num_C += 1
    else:
        num_G += 1


print('Number of T bases in the FRAT1 gene: ', num_T)

if (num_T > num_A) and (num_T > num_C) and (num_T > num_G):
    x = 'Timine'
elif (num_A > num_T) and (num_A > num_C) and (num_A > num_G):
    x = 'Adenine'
elif (num_G > num_T) and (num_G > num_A) and (num_G > num_C):
    x = 'Guanine'
else:
    x = 'Citosine'

print('The most abundant base is: ', x)


def perc(base):
    seq_len = len(seq)
    result = 0
    for x in seq:
        if x == base:
            result += 1
    if seq_len > 0:
        per = round(100.0 * result / seq_len, 1)
    else:
        per = 0
    return per

per_A = perc('A')
per_T = perc('T')
per_G = perc('G')
per_C = perc('C')

print('The percentage of A is: ', per_A)
print('The percentage of T is: ', per_T)
print('The percentage of G is: ', per_G)
print('The percentage of C is: ', per_C)
