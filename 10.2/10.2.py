name = input("Enter file: ")
tim = dict()

try:
    handle = open(name)
except:
    print('Wrong file name:', name)
    quit()

for line in handle:

    if not line.startswith('From '):
        continue

    items = line.split()
    item = items[5]

    hours = item.split(':')
    hour = hours[0]

    tim[hour] = tim.get(hour, 0) + 1

vals = sorted((key, val) for key, val in tim.items())

for k, v in vals:
    print(k, v)
