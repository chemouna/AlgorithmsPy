# square root using binary search
def sqrt(n):
    if n < 0:
        raise ValueError
    if n == 1 or n == 0:
        return n
    low = 0
    high = 1 + (n / 2)
    while low < high:
        mid = low + (high - low) / 2
        s = mid ** 2
        if s == n:
            return mid
        elif s < n:
            low = mid
        else:
            high = mid


print(sqrt(0))
print(sqrt(16))
print(sqrt(25))
print(sqrt(36))
print(sqrt(64))
