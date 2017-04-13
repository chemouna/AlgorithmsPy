

def solve():
    smallest = 100
    for a in range(100, 999):
        for b in range(1000 - a, 999):
            c = a + b
            if c > 999 and is_pandigital(a, b, c):
                smallest = min(a, b, smallest)
    return smallest


def is_pandigital(a, b, c):
    presence = [False] * 10
    for x in (a, b, c):
        while x > 0:
            q = x / 10
            r = x % 10
            if presence[r]:
                return False
            else:
                presence[r] = True
                x = q

    for x in range(0, 9):
        if not presence[r]:
            return False

    return True

print(solve())