# Number Puzzle: https://programmingpraxis.com/2015/07/21/a-number-puzzle/

from itertools import permutations


def solution(n):
    Q = [(k, 1, {k}) for k in list(range(1, 10))]
    while Q:
        k, div, s = Q.pop()
        if k % div == 0:
            if div == n:
                yield k
            else:
                Q += [(10 * k + m, div + 1, s | {m})
                      for m in range(10) if m not in s]
    return Q


def solution2(n):
    for p in permutations("0123456789"):
        if all(int("".join(p[:i])) % i == 0 for i in range(1, 11)):
            print(int("".join(p)))

print(solution(10))
# print(solution2(10))


