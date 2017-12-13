
import random

def generate_array(item_count, lower_bound, upper_bound):
    number_list = []
    for x in range(1, item_count):
        number_list.append(random.randint(lower_bound, upper_bound))
    return number_list


# using divide and conquer
def max_subarray_divide_and_conquer(arr):
    helper_max_subarray_div_conquer(arr, 0, (len(arr) - 1))


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

    return max(lmax + rmax, helper_max_subarray_div_conquer(arr, l, m), helper_max_subarray_div_conquer(arr, m + 1, r))


# using kadane algorithm
def max_subarray_kadane(arr):
    max_so_far = max_ending_here = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


magnitude = input('enter vector size: ')
number_list = generate_array(magnitude, -10, 10)

print "divide and conquer:"
print max_subarray_divide_and_conquer(number_list)

print "kadane:"
print max_subarray_kadane(number_list)
