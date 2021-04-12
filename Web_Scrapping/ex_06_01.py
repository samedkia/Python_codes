import urllib.request, urllib.parse, urllib.error
import json
import ssl

# this program takes the numbers as count from  json and sum them.
# igonre ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a link: ')
file = urllib.request.urlopen(url, context=ctx)
data = file.read()
js = json.loads(data)

lst = list()
for key in js:
    numbs = js['comments']
for numb in numbs:
    x = numb['count']
    lst.append(x)
print(sum(lst))
