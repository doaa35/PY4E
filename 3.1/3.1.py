hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))

if hours<=40:
    print(hours * rate)
else:
    print(40*rate + (hours-40)*1.5*rate)
