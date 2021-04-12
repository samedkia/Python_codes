import urllib.request, urllib.parse, urllib.error
import json
import ssl

# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON

# Ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
if api_key is False:
    api_key = 42
    link = 'http://py4e-data.dr-chuck.net/json?'
else:
    link = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('enter address: ')
    if (len(address))<1:
        break

    dic = dict()
    dic['address'] = address
    if api_key is not False:
        dic['key'] = api_key
    url = link + urllib.parse.urlencode(dic)
    file = urllib.request.urlopen(url, context=ctx)
    data = file.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    p_id = js['results'][0]['place_id']
    print(p_id)
    # print(json.dumps(js, indent=2))
