# Do a variation with more than two arrays
# Reduction steps:
#
# If mid index of a + mid index of b is less than k
#   If mid element of a is greater than mid element of b, we can ignore the first half of b, adjust k.
#   else ignore the first half of a, adjust k.
# Else if k is less than sum of mid indices of a and b:
#   If mid element of a is greater than mid element of b, we can safely ignore second half of a
#   else we can ignore second half of b


def kthlargest(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k]
    if len(arr2) == 0:
        return arr1[k]

    mid1 = len(arr1) / 2
    mid2 = len(arr2) / 2
    if mid1 + mid2 < k:
        if arr1[mid1] > arr2[mid2]:
            kthlargest(arr1, arr2[mid2 + 1:], k - mid2 - 1)
        else:
            kthlargest(arr1[mid1 + 1:], arr2, k - mid1 - 1)
    elif mid1 + mid2 > k:
        if arr1[mid1] > arr2[mid2]:
            kthlargest(arr1[:mid1], arr2, k)
        else:
            kthlargest(arr1, arr2[:mid2], k)
