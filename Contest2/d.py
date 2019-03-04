n = int(input())

first = 0
second = 1
for i in range(n):
    first, second = second, first + second
print(first)
