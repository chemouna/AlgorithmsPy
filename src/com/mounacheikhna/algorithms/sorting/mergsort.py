from heapq import merge


def mergeSort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = mergeSort(left)
    right = mergeSort(right)
    return list(merge(left, right))


a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = mergeSort(a)
print a