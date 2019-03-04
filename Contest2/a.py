n = int(input())

for i in range(1, n+1):
    end = '\n' if i == n else ', '
    if i % 15 == 0:
        print('Fizz Buzz', end=end)
    elif i % 3 == 0:
        print('Fizz', end=end)
    elif i % 5 == 0:
        print('Buzz', end=end)
    else:
        print(i, end=end)
