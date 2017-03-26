from collections import defaultdict


def lcs(xs, ys):
    """
    Return a longest common subsequence of xs and ys.
    """
    if xs and ys:
        *xb, xe = xs  # split xs into its beginning, xb, and its final element xe
        *yb, ye = ys
        if xe == ye:
            return lcs(xb, yb) + [xe]
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

# lcs, calls = count_lcs_calls(lcs)
# print(lcs("HUMAN", "CHIMPANZEE"))


# print(lcs('MAN', 'PIG'))
# print(*sorted((v, k) for k, v in calls.items()), sep='\n')
# calls.clear()

# print(lcs('CHIMP', 'CHIMP'))
# print(*sorted((v, k) for k, v in calls.items()), sep='\n')

# print(lcs('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA', 'GTCGTTCGGAATGCCGTTGCTCTGTAAA')) # because of the number
# of the recursion calls this call takes a very long time.

def memoize(fn):
    """
    Return a memoized version of the input function.

    The returned function caches the results of previous calls.
    Useful if a function call is expensive, and the function
    is called repeatedly with the same arguments.
    """
    cache = dict()

    def wrapped(*v):
        key = tuple(v)  # tuples are hashable, and can be used as dict keys
        if key not in cache:
            cache[key] = fn(*v)
        return cache[key]

    return wrapped


def memoizedLcs(xs, ys):
    """
    Return a longest common subsequence of xs and ys.
    """

    @memoize
    def lcs_(i, j):
        if i and j:
            xe, ye = xs[i - 1], ys[j - 1]
            if xe == ye:
                return lcs_(i - 1, j) + [xe]
            else:
                return max(lcs_(i - 1, j), lcs_(i, j - 1))
        else:
            return []

    return lcs_(len(xs), len(ys))


# print(memoizedLcs("HUMAN", "CHIMPANZEE"))
# ss = lcs('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA', 'GTCGTTCGGAATGCCGTTGCTCTGTAAA')
# print(''.join(ss))


# but the memoized version will soon hit the recursion limit

def lcsDp(a, b):
    matrix = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                matrix[i + 1][j + 1] = matrix[i][j] + 1
            else:
                matrix[i + 1][j + 1] = max(matrix[i][j + 1], matrix[i + 1][j])

    # read the lcs itself
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if matrix[x][y] == matrix[x - 1][y]:
            x -= 1
        elif matrix[x][y] == matrix[x][y - 1]:
            y -= 1
        else:
            result = a[x - 1] + result
            x -= 1
            y -= 1
    return result

print(lcsDp("HUMAN", "CHIMPANZEE"))
print(lcsDp('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA', 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'))
