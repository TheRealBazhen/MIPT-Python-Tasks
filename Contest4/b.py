import heapq


def merge_sorter(*args):
    iters = [iter(arg) for arg in args]
    values = []
    for num in range(len(iters)):
        try:
            val = next(iters[num])
        except StopIteration:
            continue
        values.append((val, num))
    heapq.heapify(values)
    while values:
        val, num = heapq.heappop(values)
        yield val
        try:
            new_val = next(iters[num])
        except StopIteration:
            continue
        heapq.heappush(values, (new_val, num))


def gen():
    i = 2
    while True:
        yield i
        i += 1


def one():
    yield 1


for i in merge_sort(range(3, 10, 2), [3, 6, 9, 11, 11, 45, 123], []):
    print(i)
