total = int(input())
count = int(input())
priceSum = 0

for i in range(1, count+1):
    price, ea = input().split()
    price = int(price)
    ea = int(ea)
    priceSum += price * ea

if priceSum == total:
    print("Yes")
else:
    print("No")