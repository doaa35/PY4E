fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Wrong file name:', fname)

lst = list()
for line in fh:
    element = line.rstrip().split()
    for i in element:
        if i not in lst:
            lst.append(i)
        else:
            continue
lst.sort()
print(lst)
