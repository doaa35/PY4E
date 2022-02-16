import urllib.parse, urllib.request
import xml.etree.ElementTree as ET

url = input('Enter URL: ')

url_open = urllib.request.urlopen(url)
data = url_open.read()

tree = ET.fromstring(data)

com = tree.findall('comments/comment')
sum = 0

for i in com:
    num = i.find('count').text
    count = int(num)
    sum = sum +count

print(sum)
