def hasArrayTwoCandidates(arr, arr_size, x):
    quicksort(arr, 0, arr_size - 1)
    l = 0
    r = arr_size - 1
    while l < r:
        if arr[l] + arr[r] == x:
            return 1
        elif arr[l] + arr[r] < x:
            l += 1
        else:
            r -= 1
    return 0


def quicksort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quicksort(arr, l, p - 1)
        quicksort(arr, p + 1, r)


def partition(arr, l, r):
    v = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= v:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


A = [1, 4, 45, 6, 10, -8]
n = 16
if hasArrayTwoCandidates(A, len(A), n):
    print("Array has two elements with the given sum")
else:
    print("Array doesn't have two elements with the given sum")
