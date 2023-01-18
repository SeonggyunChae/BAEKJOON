number = int(input())
count = int(1)
num4 = int(number)

while 1:
    num1 = int(num4//10)
    num2 = int(num4%10)
    num3 = int(num1 + num2)
    num4 = int(num2*10 + num3%10)

    if number == num4:
        break
    else:
        count += 1
        
print(count)