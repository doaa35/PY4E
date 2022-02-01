from tkinter import N
from tracemalloc import start
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter repeat time: '))
position = int(input('Enter position: '))

htm = urlopen(url, context=ctx).read()
soup = BeautifulSoup(htm,'html.parser')

href = soup.find_all('a')
for i in range(count):
    forward_link = href[position-1].get('href', None)
    print(href[position-1].contents[0])
    htm = urlopen(forward_link, context=ctx).read()
    soup = BeautifulSoup(htm,'html.parser')
    href = soup.find_all('a')