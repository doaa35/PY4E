fname = input("Enter file name: ")
count = 0

try:
    fh = open(fname)
except:
    print('Wrong file name:', fname)
    quit()

for line in fh:
    if not line.startswith('From '):
        continue
    count += 1
    element = line.rstrip().split()
    print(element[1])

print("There were", count, "lines in the file with From as the first word")
