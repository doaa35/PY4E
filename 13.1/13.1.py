import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user>
            <name>Doaa</name>
            <id>005</id>
        </user>
        <user>
            <name>Doha</name>
            <id>0010</id>
        </user>
    </users>
</stuff>

'''

tree = ET.fromstring(input)
lst = tree.findall('users/user')

for i in lst:
    print('Name: ', i.find('name').text)
    print('id: ', i.find('id').text)
