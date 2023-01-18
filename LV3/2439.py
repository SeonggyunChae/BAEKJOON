count = int(input())
a = count

for i in range(1, count+1):
    a -= 1
    print(" "*a, "*"*i, sep="")
