n = int(input())

ind = 1
num = 2
while ind < n:
    num += 1
    while True:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            break
        num += 1
    ind += 1
print(num)
