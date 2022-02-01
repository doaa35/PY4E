from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
htm = urlopen(url, context=ctx).read()

soup = BeautifulSoup(htm,'html.parser')

sum = 0
for tag in soup.find_all('span'):
    sum = sum + int(tag.contents[0])
print(sum)