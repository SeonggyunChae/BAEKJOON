hour, min= input().split()

hour = int(hour)
min = int(min)

if min >= 45:
    min -= 45
    print(hour, min)
else:
    min += 15
    if hour == 0:
        hour = 23
        print(hour, min)
    else:
        hour -= 1
        print(hour, min)