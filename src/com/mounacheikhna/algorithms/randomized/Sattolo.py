from random import randrange


def sattoloCycle(items):
    i = len(items)
    while i > 1:
        i -= 1
        j = randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]


