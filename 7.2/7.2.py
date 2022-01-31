fname = input("Enter file name: ")
count = 0
total = 0
try:
    fh = open(fname)
except:
    print('Wrong file: ', fname)
    quit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    count += 1
    line = line.rstrip()
    fl = line.find('0')
    flNumber = line[fl+1:]
    total = total + float(flNumber)

print('Average spam confidence:', total/count)