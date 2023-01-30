n, x = input().split()
numbers = input().split()
a = []

for i in numbers:
    if int(i) < int(x):
        a.append(i)

print(*a)