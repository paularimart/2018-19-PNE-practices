import http.client
import json

HOSTNAME = "api.icndb.com"
ENDPOINT_NUMBER = "/jokes/count"
ENDPOINT_CATEGORIES = "/categories"
ENDPOINT_RANDOM = "/jokes/random"
METHOD = "GET"
JOKE_ID = "?"

headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT_NUMBER, None, headers)

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

# -- Generate the object from the json file
chuck = json.loads(text_json)

num = chuck['value']

print()
print("Number of jokes: {}".format(num))

conn.request(METHOD, ENDPOINT_CATEGORIES, None, headers)

# -- Wait for the server's response
r2 = conn.getresponse()

# -- Read the response's body and close
# -- the connection
text_json = r2.read().decode("utf-8")
conn.close()

# -- Generate the object from the json file
chuck = json.loads(text_json)

categories = chuck['value']

print()
print("Number of categories: {}".format(len(categories)))
print("Categories: {}".format(categories))

conn.request(METHOD, ENDPOINT_RANDOM, None, headers)

# -- Wait for the server's response
r3 = conn.getresponse()

# -- Read the response's body and close
# -- the connection
text_json = r3.read().decode("utf-8")
conn.close()

# -- Generate the object from the json file
chuck = json.loads(text_json)

random = chuck['value']
joke = random['joke']

print()
print("Random joke: {}".format(joke))
