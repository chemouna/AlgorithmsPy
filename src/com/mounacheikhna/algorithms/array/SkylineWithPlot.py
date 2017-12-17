import sys
from matplotlib import pylab


def main():
    pass


if __name__ == '__main__':
    main()

startL1 = startL2 = endL1 = endL2 = heightL1 = heightL2 = 0


class Skyline:
    startL1 = 0
    startL2 = 0
    endL1 = 0
    endL2 = 0
    heightL1 = 0
    heightL2 = 0

    def __init__(self):
        pass

    def update(self, list1, list2, i, j):
        self.startL1 = list1[i][0]
        self.startL2 = list2[j][0]
        self.endL1 = list1[i][1]
        self.endL2 = list2[j][1]
        self.heightL1 = list1[i][2]
        self.heightL2 = list2[j][2]

    def merge(self, list1, list2):
        i = j = 0
        finalList = []
        while True:
            if j == len(list2):
                finalList.extend(list1[i:])
                return finalList
            if i == len(list1):
                finalList.extend(list2[j:])
                return finalList

            self.update(list1, list2, i, j)

            if not self.doesOverlap(list1[i], list2[j]):
                if startL1 < startL2:
                    i = i + 1
                    finalList.append((self.startL1, self.endL1, self.heightL1))
                else:
                    j = j + 1
                    finalList.append((self.startL2, self.endL2, self.heightL2))
                continue

            if self.startL1 < self.startL2:
                if (self.endL1 >= self.endL2) and (self.heightL1 >= self.heightL2):
                    finalList.append((self.startL1, self.endL1, self.heightL1))
                    j = j + 1
                    i = i + 1
                    if j != len(list2):
                        list2[j] = (self.endL1, list2[j][1], list2[j][2])
                    continue
                finalList.append((startL1, min(self.endL1, startL2), heightL1))
                if self.endL1 < self.startL2:
                    i = i + 1
                else:
                    newVal = list2[j][0]
                    list1[i] = (newVal, list1[i][1], list1[i][2])
                continue

            if startL2 < startL1:
                if (self.endL1 <= self.endL2) and (self.heightL1 <= self.heightL2):
                    finalList.append((startL2, endL2, heightL2))
                    i = i + 1
                    j = j + 1
                    if i != len(list1):
                        list1[i] = (self.endL2, list1[i][1], list1[i][2])
                    continue
                finalList.append((self.startL2, min(self.endL2, self.startL1), self.heightL2))
                if self.endL2 < self.startL1:
                    j = j + 1
                else:
                    newVal = list1[i][0]
                    list2[j] = (newVal, list2[j][1], list2[j][2])
                continue

            if self.startL1 == self.startL2:
                if self.heightL1 >= self.heightL2:
                    finalList.append((self.startL1, self.endL1, heightL1))
                    if self.endL1 > self.endL2:
                        j = j + 1
                        i = i + 1
                    if self.endL1 < self.endL2:
                        i = i + 1
                        list2[j] = (self.endL1, list2[j][1], list2[j][2])
                if self.heightL2 > self.heightL1:
                    finalList.append((self.startL1, self.endL2, self.heightL2))
                    if self.endL1 < self.endL2:
                        i = i + 1
                        j = j + 1
                    if self.endL2 < self.endL1:
                        j = j + 1
                        list1[i] = (self.endL2, list1[i][1], list1[i][2])
                    continue

        return self.compress(finalList)

    def compress(self, l):
        final = []
        i = 1
        while True:
            if i > len(l): break
            if i == len(l):
                final.append(l[i - 1])
                break

            prev = l[i - 1]
            curr = l[i]
            # if prev's end marker == start marker of current AND height of both the same -- then coalesce prev and curr
            if (prev[1] == curr[0]) and (prev[2] == curr[2]):  # height of the curr block is < prev - just merge
                prev = (prev[0], curr[1], prev[2])
                final.append(prev)
                i += 2
            elif (prev[1] == curr[1]) and (prev[2] >= curr[2]):  # height of the curr block is < prev - just merge
                prev = (prev[0], curr[1], prev[2])
                final.append(prev)
                i += 2
            else:
                final.append(prev)
                i += 1
        return final

    def doesOverlap(self, l1, l2):
        s1 = l1[0]
        e1 = l1[1]
        s2 = l2[0]
        e2 = l2[1]

        if s2 >= e1:
            return False
        if s1 >= e2:
            return False
        return True

    def skyline(self, lst):
        if len(lst) == 2:
            return self.merge([lst[0]], [lst[1]])
        else:
            lengthOfList = len(lst)
            l1 = self.skyline(lst[:lengthOfList / 2])
            l2 = self.skyline(lst[lengthOfList / 2:])
            return self.merge(l1, l2)

    def showSkyline(self, l):
        pylab.cla()
        for tpl in l:
            st = tpl[0]
            end = tpl[1]
            height = tpl[2]
            pylab.bar(st, height, (end - st))
        pylab.show()
        print "Done"


row = []
print len(sys.argv)
if (len(sys.argv) - 1) % 3 != 0:
    print "Each tuple has 3 coordinates - the number of params entered should be multiple of 3"
    sys.exit()

for i in range(1, len(sys.argv) / 3 + 1):
    x1 = int(sys.argv[3 * (i - 1) + 1])
    x2 = int(sys.argv[3 * (i - 1) + 2])
    h1 = int(sys.argv[3 * (i - 1) + 3])

    if x1 < 0 or x2 < 0 or h1 < 0:
        print "Each tuple value needs to be a +ve integer"
        sys.exit()
    row.append((x1, x2, h1))

sl = Skyline()
cl = sl.compress(sl.skyline(row))
print cl
sl.showSkyline(cl)
