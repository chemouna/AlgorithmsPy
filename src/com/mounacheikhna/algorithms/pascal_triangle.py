import collections


# recursive solution
def value(row, index):
    if index < 0 or index > row:
        return 0
    if index == 0 or index == row:
        return 1
    return value(row - 1, index) + value(row - 1, index - 1)


def row(n):
    return [value(n, x) for x in range(0, n + 1)]


for i in range(10):
    print(row(i))

# With memoization
values = collections.defaultdict(dict)


def value_mem(row, index):
    result = values[row].get(index)
    if result is not None:
        return result
    if index < 0 or index > row:
        return 0
    if index == 0 or index == row:
        return 1
    result = value(row - 1, index) + value(row - 1, index - 1)
    values[row][index] = result
    return result

# Dynamic Programming (we can notice that for each row we need only information from the previous row)
prev = []
for row in range(20):
    curr = [1]
    for index in range(1, row):
        curr.append(prev[index - 1] + prev[index])
    curr.append(1)
    print(curr)
    prev = curr

