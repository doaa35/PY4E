score = float(input("Enter Score: "))

if score < 0.0 or score > 1.0:
    print('Out of range')
    quit()

else:
    if score >= 0.9:
        print('A')
    elif score in (0.8, 0.9):
        print('B')
    elif score in (0.7, 0.8):
        print('C')
    elif score in (0.6, 0.7):
        print('D')
    elif score < 0.6:
        print('F')
