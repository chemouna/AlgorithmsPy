class RollingHash:
    def __init__(self, string, size):
        self.str = string
        self.hash = 0

        for i in xrange(0, size):
            self.hash += ord(self.str[i])

        self.init = 0
        self.end = size

    # Note that this rolling hash is very simple and does not handle many cases like integer overflow f.ex
    def update(self):
        if self.end <= len(self.str) - 1:
            self.hash -= ord(self.str[self.init])
            self.hash += ord(self.str[self.end])
            self.init += 1
            self.end += 1

    def digest(self):
        return self.hash

    def text(self):
        return self.str[self.init:self.end]


def rabin_karp(substring, string):
    if substring is None or string is None:
        return -1
    if substring == "" or string == "":
        return -1

    if len(substring) > len(string):
        return -1

    hs = RollingHash(string, len(substring))
    hsub = RollingHash(substring, len(substring))
    hsub.update()

    for i in range(len(string) - len(substring) + 1):
        if hs.digest() == hsub.digest():
            if hs.text() == substring:
                return i
        hs.update()

    return -1


print(rabin_karp("H", "Hello World"))
print(rabin_karp("ell", "Hello World"))
print(rabin_karp("Wo", "Hello World"))
print(rabin_karp("ttt", "Hello World"))
