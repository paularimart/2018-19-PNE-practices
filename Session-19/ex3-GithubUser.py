import http.client
import json

HOSTNAME = "api.github.com"
METHOD = "GET"
ENDPOINT = "/users/"
ENDPOINT_REPOS = "/repos/"

user = input("Type a username: ")

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + user, None, headers)

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

page = json.loads(text_json)
name = page['name']

print('The real name of the user is: {}'.format(name))

conn.request(METHOD, ENDPOINT + user + "/repos", None, headers)

r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

page = json.loads(text_json)

print()
print("Repositories of this user: ")
for x in page:
    print(x['name'])

conn.request(METHOD + ENDPOINT_REPOS + user + "/2018-19-PNE-practices/contributors", None, headers)

r2 = conn.getresponse()

text_json = r2.read().decode("utf-8")
conn.close()

page = json.loads(text_json)
list = page[0]
contributions = list['contributions']

print('Number of commits to the 2018-19-PNE-repo: {}'.format(contributions))

