# coding=utf-8
import random


def eratosthenes(n):
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))


print list(eratosthenes(50))

_mrpt_num_trials = 5  # number of bases to test

# coding=utf-8

# Algorithm:
#
# Input: n > 2, an odd integer to be tested for primality;
# Output: composite if n is composite, otherwise probably prime
# write n − 1 as 2^s . d with d odd by factoring powers of 2 from n − 1
# LOOP: repeat k times:
#    pick a randomly in the range [2, n − 1]
#    x ← a^d mod n
#    if x = 1 or x = n − 1 then do next LOOP
#    for r = 1 .. s − 1
#       x ← x^2 mod n
#       if x = 1 then return composite
#       if x = n − 1 then do next LOOP
#    return composite
# return probably prime
import random


def is_primer_miller_rabin(n, k=10):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True


print is_primer_miller_rabin(100 ** 10 - 1)


def twinPrimes(num):
    primesList = []
    if num >= 5:
        primesList.append((3, 5))
    if num >= 7:
        primesList.append((5, 7))
    for x in range(0, num + 1, 30):  # why 30 ?
        if is_primer_miller_rabin(x - 1) and is_primer_miller_rabin(x + 1):
            primesList.append((x - 1, x + 1))
        if is_primer_miller_rabin(x + 11) and is_primer_miller_rabin(x + 13) and num >= x + 11:
            primesList.append((x + 11, x + 13))
        if is_primer_miller_rabin(x + 17) and is_primer_miller_rabin(x + 19) and num >= x + 19:
            primesList.append((x + 17, x + 19))
    return primesList