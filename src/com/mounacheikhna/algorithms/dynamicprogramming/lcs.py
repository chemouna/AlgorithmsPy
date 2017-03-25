from collections import defaultdict


def lcs(xs, ys):
    """
    Return a longest common subsequence of xs and ys.
    """
    if xs and ys:
        *xb, xe = xs  # split xs into its beginning, xb, and its final element xe
        *yb, ye = ys
        if xe == ye:
            return lcs(xb, ys) + [xe]
        else:
            return max(lcs(xb, ys), lcs(xs, yb))
    else:
        return []


concat = ''.join


def count_lcs_calls(lcs):
    """
    Return a pair (lcs, calls)

    Where:
    lcs - a wrapped version of lcs, which counts up calls
    calls - a dict mapping arg pairs to the number of times lcs
    has been called with these args.
    """
    calls = defaultdict(int)

    def wrapped(xs, ys):
        calls[(concat(xs), concat(ys))] += 1
        return lcs(xs, ys)

    return wrapped, calls


lcs, calls = count_lcs_calls(lcs)

# print(lcs("HUMAN", "CHIMPANZEE"))

# print(lcs('MAN', 'PIG'))
# print(*sorted((v, k) for k, v in calls.items()), sep='\n')

print(lcs('CHIMP', 'CHIMP'))
print(*sorted((v, k) for k, v in calls.items()), sep='\n')
