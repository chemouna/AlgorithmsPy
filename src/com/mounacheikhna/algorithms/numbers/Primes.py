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
def is_probable_prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient

    # test the base a to see whether we 'find' compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True  # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True
