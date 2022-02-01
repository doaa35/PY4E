name = input("Enter file: ")
email = dict()
bigVal = None
bigKey = None

try:
    handle = open(name)
except:
    print('Wrong file name:', name)
    quit()

for line in handle:

    if not line.startswith('From '):
        continue

    words = line.split()
    word = words[1]
    email[word] = email.get(word, 0) + 1

    for key, val in email.items():
        if bigVal is None or val > bigVal:
            bigVal = val
            bigKey = key

print(bigKey, bigVal)