big = None
small = None

while True:
    data = input("Enter a number: ")

    if data == 'done':
        break

    try:
        num = float(data)
    except:
        print('Invalid input')
        continue

    if small is None or small > num:
        small = num

    elif big is None or big < num:
        big = num

print('Maximum is', int(big))
print('Minimum is', int(small))
