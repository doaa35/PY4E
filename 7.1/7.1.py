fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Wrong file: ', fname)
    quit()

for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)