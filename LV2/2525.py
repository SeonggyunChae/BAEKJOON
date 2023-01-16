hour, min = input().split()
timer = input()

hour = int(hour)
min = int(min)
timer = int(timer)

if (min + timer) >= 60:
    hour += (min + timer) // 60
    min = (min + timer) % 60
    if hour >= 24:
        hour -= 24
        print(hour, min)
    else:
        print(hour, min)
else:
    min += timer
    print(hour, min)