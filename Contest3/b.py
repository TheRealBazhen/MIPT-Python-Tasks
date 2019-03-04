first = input()
second = input()
dic = dict(zip(first, second))
second_len = len(second)
first_len = len(first)
for i in range(0, first_len - second_len):
    dic[first[i + second_len]] = None
print(sorted(list(dic.items())))
