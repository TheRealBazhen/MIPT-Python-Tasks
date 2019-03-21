inp = input()
str_len = len(inp)

i = 0
while i < str_len - 1:
    if inp[i:str_len - 1] == inp[str_len-1:i:-1]:
        break
    i += 1
j = 0
while j < str_len - 1:
    if inp[0:str_len - 1 - j] == inp[str_len-1 - j:0:-1]:
        break
    j += 1
print(min(i, j))
