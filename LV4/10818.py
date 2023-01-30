a = input()
numbers = input().split()

#list, String -> int
numbers = list(map(int, numbers))

print(min(numbers), max(numbers))