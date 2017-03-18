class SmartWordToy:
    def __init__(self):
        pass

    def minPresses(self, start, end, forbid):
        visited = {start}
        forbidExpanded = set()
        self.expand_forbid(forbid, forbidExpanded)

        queue = [(start, 0)]
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        while queue:
            node, presses = queue.pop()
            if node == end:
                return presses

            for i in range(len(node)):
                currentCharIndex = alphabet.index(node[i])
                for j in [-1, 1]:
                    newNode = list(node)
                    newNode[i] = alphabet[(currentCharIndex + j) % 26]
                    newNode = ''.join(newNode)
                    if newNode not in visited and newNode not in forbidExpanded:
                        visited.add(newNode)
                        queue.insert(0, (newNode, presses + 1))

        return -1

    def expand_forbid(self, forbid, res):
        for s in forbid:
            forbiddenWords = []
            forbiddenWordsList = s.split(' ')
            self.expand_forbidden_word('', forbiddenWordsList, forbiddenWords)
            for w in forbiddenWords:
                res.add(w)

    def expand_forbidden_word(self, str_so_far, remainder, res):
        if not remainder:
            res.append(str_so_far)
        else:
            nextChars = remainder[0]
            # we need to pick each character and combine it with other characters to get all forbidden word
            for c in nextChars:
                clone = list(remainder)
                clone.pop(0)
                self.expand_forbidden_word(str_so_far + c, clone, res)


swt = SmartWordToy()
print(swt.minPresses("aaaa", "zzzz",
                     ["a a a z", "a a z a", "a z a a", "z a a a", "a z z z", "z a z z", "z z a z", "z z z a"]))

print(swt.minPresses("aaaa", "bbbb", []))

print(swt.minPresses("aaaa", "mmnn", []))

print(swt.minPresses("aaaa", "zzzz", ["bz a a a", "a bz a a", "a a bz a", "a a a bz"]))

print(swt.minPresses("aaaa", "zzzz",
                ["cdefghijklmnopqrstuvwxyz a a a", "a cdefghijklmnopqrstuvwxyz a a", "a a cdefghijklmnopqrstuvwxyz a",
                 "a a a cdefghijklmnopqrstuvwxyz"]))
