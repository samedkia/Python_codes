import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter a link: ')
html = urllib.request.urlopen(url, context=ctx)
soup = BeautifulSoup(html, 'html.parser')

x = 0
tags = soup('span')
for tag in tags:
    x = x + int(tag.contents[0])
print(x)
