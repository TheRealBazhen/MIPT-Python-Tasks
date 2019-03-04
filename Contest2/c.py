n, m = [int(s) for s in input().split()]
print('\n'.join(
    [' '.join([str((i + 1) * (j + 1)) for i in range(m)]) for j in range(n)]))
