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
