import requests
import simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"
payload ={"longURL": "http://example.com"}
header = {"Content-Type": "application/json"}
r = requests.post(url, json = payload, headers = header)

print(str(r.headers))