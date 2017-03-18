

class SmartWordToy:
    def __init__(self):
        pass

    def minPresses(self, start, end, forbid):
        visited = {start}
        forbidExpanded = set()
        self.expandForbid(forbid, forbidExpanded)


    def expandForbid(self, forbid, res):
        for str in forbid:
            forbiddenWords = []
            forbiddenWordsList = str.split(' ')
            self.expandForbiddenWord(' ', forbiddenWordsList, forbiddenWords)
            for s in forbiddenWords:
                res.add(s)

    def expandForbiddenWord(self, strSoFar, remainder, res):
        if not remainder:
            res.append(strSoFar)
        else:
            nextChars = remainder[0]
            # we need to pick each character and combine it with other characters to get all forbidden word
            for c in nextChars:
                clone = list(remainder)
