num = int(input())

diff = -1
while True:
    diff += 1
    a = num + diff
    digs = [a // 100000, (a // 10000) % 10, (a // 1000) % 10,
            (a // 100) % 10, (a // 10) % 10, a % 10]
    if digs[0] + digs[1] + digs[2] == digs[3] + digs[4] + digs[5]:
        break
    if diff > num:
        continue
    a = num - diff
    digs = [a // 100000, (a // 10000) % 10, (a // 1000) % 10,
            (a // 100) % 10, (a // 10) % 10, a % 10]
    if digs[0] + digs[1] + digs[2] == digs[3] + digs[4] + digs[5]:
        break

print(''.join([str(d) for d in digs]))
