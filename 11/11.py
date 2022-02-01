import re
file = open('actual_data.txt')
sum = 0
for line in file:
    line = line.rstrip()
    nums = re.findall('([0-9]+)', line)
    for val in nums:
        int_vals = int(val)
        sum = sum + int_vals
print(sum)
