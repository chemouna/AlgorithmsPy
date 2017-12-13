# using divide and conquer
def max_subarray_divide_and_conquer(arr):
    helper_max_subarray_div_conquer(arr, 0, arr.length - 1)


def helper_max_subarray_div_conquer(arr, l, r):
    if l > r:  # 0 elements
        return 0
    if l == r:  # 1 element
        return max(0, arr[l])
    m = (l + r) / 2
    lmax = sum = 0
    for i in range(l, m):  # left side
        sum += arr[i]
        lmax = max(sum, lmax)

    rmax = sum = 0
    for i in range(m + 1, r):
        sum += arr[i]
        rmax = max(sum, rmax)

    return max(lmax + rmax, helper_max_subarray_div_conquer(l, m), helper_max_subarray_div_conquer(m + 1, r))


# using kadane algorithm
def max_subarray(arr):
    max_so_far = max_ending_here = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
