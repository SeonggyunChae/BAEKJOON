a = input()
sum = []

a = int(a)

for i in range(1, a+1):
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    sum.append(num1 + num2)\

for i in range(0, a):
    print(sum[i])
