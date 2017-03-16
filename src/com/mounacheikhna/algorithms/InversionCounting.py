# !/usr/bin/python
def divide(a):
    half = len(a) / 2
    return [a[:half], a[half:]]


def merge_and_count(left, right):
    x = []
    leftIndex = 0
    rightIndex = 0
    invCount = 0
    size1 = len(left)
    size2 = len(right)
    while leftIndex < size1 and rightIndex < size2:
        if left[leftIndex] <= right[rightIndex]:
            x.append(left[leftIndex])
            leftIndex += 1
        else:
            x.append(right[rightIndex])
            rightIndex += 1
            invCount += size1 - leftIndex

    for i in range(leftIndex, size1):
        x.append(left[i])

    for i in range(rightIndex, size2):
        x.append(right[i])

    return x, invCount


def inversion_count(a):
    if len(a) > 1:
        (left, right) = divide(a)
        left, leftInv = inversion_count(left)
        right, rightInv = inversion_count(right)

        merged, inv = merge_and_count(left, right)
        return merged, (inv + leftInv + rightInv)
    else:
        return a, 0


a = [6, 5, 4, 3, 2, 1]
print
'before sorting', a
r = inversion_count(a)
print
'after sorting', r
