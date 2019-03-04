from collections import Counter

words = input().split()
num_words = len(words)
words_count = Counter(words)
print(sorted(list(words_count.values()))[-1] / num_words)
