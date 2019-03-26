import http.client
import json

HOSTNAME = "www.metaweather.com"
ENDPOINT_SEARCH_WOEID = "/api/location/search/"
ENDPOINT = "/api/location/"
METHOD = "GET"

request = input("Type a city: ")

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT_SEARCH_WOEID + 'search/?query=' + request, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

city = json.loads(text_json)
woeid = city['woeid']

print('The woeid is: {}'.format(woeid))
