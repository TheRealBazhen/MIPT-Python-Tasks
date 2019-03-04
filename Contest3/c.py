from collections import Counter

string = input()
sublen = int(input())
substrs = [string[i:i+sublen] for i in range(0, len(string) - sublen + 1)]
count = Counter(substrs)
print(sorted([substr for (substr, count) in list(count.items()) if count > 1]))
