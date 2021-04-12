import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.veify_mode = ssl.CERT_NONE

url = input('Enter a link: ')
data = urllib.request.urlopen(url, context=ctx).read()

x = 0
tree = ET.fromstring(data)
stuffs = tree.findall('comments/comment/count')
for stuff in stuffs:
    x = x + int(stuff.text)
print('sum is equal to:', x)
