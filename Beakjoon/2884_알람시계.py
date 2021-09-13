hh, mm = input().split()
hh = int(hh); mm = int(mm)

if mm > 44:
    print(hh, mm-45)
elif hh > 0 and mm < 45:
    print(hh-1, mm+15)
else:
    print(23, mm+15)