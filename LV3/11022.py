count = int(input())
sum = []
num1List = []
num2List = []

for i in range(1, count+1):
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)

    num1List.append(num1)
    num2List.append(num2)
    sum.append(num1 + num2)

for i in range(0, count):
    print("Case #%d:" %int(i+1), num1List[i], "+", num2List[i], "=", sum[i])