num1 = 1
num2 = 1
num1List = []
num2List = []
sum = []

while num1 != 0 and num2 != 0:
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)

    num1List.append(num1)
    num2List.append(num2)
    sum.append(num1 + num2)

for i in range(0, len(sum)-1):
    print(sum[i])