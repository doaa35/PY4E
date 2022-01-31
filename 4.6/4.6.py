def computepay(h, r):
    if h <= 40:
        return (h * r)
    else:
        return (40*r + (h-40)*1.5*r)


hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))

print("Pay", computepay(hours, rate))
