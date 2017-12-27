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


def miller_rabin_test(n, k=10):
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


print miller_rabin_test(100 ** 10 - 1)
