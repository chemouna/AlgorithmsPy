# https://programmingpraxis.com/2012/11/16/list-intersection-and-union/

# O(n^2) solution
def intersection_o_n2(l1, l2):
    """Calculate the intersection of two lists using nested loops (O(n^2) solution)."""

    result = []
    for e in l1:
        if e in l2:
            result.append(e)

    return result


# O(n log n ) solution
def intersection_o_n_logn(l1, l2):
    """Calculate the intersection of two lists in O(n log n)."""

    l1 = sorted(l1)
    l2 = sorted(l2)
    result = []

    i, j = 0, 0
    while True:
        if i >= len(l1):
            break
        elif j >= len(l2):
            break
        elif l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            result.append(l1[i])
            i += 1
            j += 1
    return result


# O(n) solution
def intersection_o_n(l1, l2):
    """Calculate the intersection of two lists in O(n)."""

    l2_set = set(l2)
    result = []

    for e in l1:
        if e in l2_set:
            result.append(e)
    return result
