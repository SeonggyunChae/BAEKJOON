a = input()
numbers = input().split()
b = input()
cnt = 0

for i in numbers:
    if int(i) == int(b):
        cnt += 1

print(cnt)
