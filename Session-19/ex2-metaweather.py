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
conn.request(METHOD, ENDPOINT_SEARCH_WOEID + '?query=' + request, None, headers)

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
list = city[0]
woeid = list['woeid']

print('The woeid is: {}'.format(woeid))

conn.request(METHOD, ENDPOINT + str(woeid) + '/', None, headers)

r2 = conn.getresponse()

text_json = r2.read().decode("utf-8")
conn.close()

city = json.loads(text_json)
current_time = city['time']

print('The current time is: {}'.format(current_time))

conn.request(METHOD, ENDPOINT + str(woeid) + '/', None, headers)

r3 = conn.getresponse()

text_json = r3.read().decode("utf-8")
conn.close()

city = json.loads(text_json)
weather = city['consolidated_weather']
list = weather[0]
temperature = list['the_temp']

print('The temperature is: {}'.format(temperature))

conn.request(METHOD, ENDPOINT + str(woeid) + '/', None, headers)

r2 = conn.getresponse()

text_json = r2.read().decode("utf-8")
conn.close()

city = json.loads(text_json)
sunset = city['sun_set']

print('The sunset will be at: {}'.format(sunset))