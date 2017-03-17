import heapq
import math


class Node(object):
    def __init__(self, weapons, shots):
        self.weapons = weapons
        self.shots = shots

    def __lt__(self, other):
        return self.shots < other.shots


class KiloManX:
    def leastShots(self, damageChart, bossHealth):
        pq = []
        # represent each weapon as a bit in an integer, we will have to store a maximum of 32,768 values
        # (2^15, as there is a maximum of 15 weapons). So we can make our visited array simply be an
        # array of 32,768 booleans.
        visited = []
        top = Node(0, 0)
        heapq.heappush(pq, top)

        m = len(damageChart)
        numWeapons = len(damageChart[0])
        nn = 1 << 15
        for i in range(nn):
            visited.append(False)

        while pq:
            top = heapq.heappop(pq)

            # make sure we don't visit the same configuration twice
            if visited[top.weapons]:
                pass

            # To check if we have all the weapons which means we defeated all bosses
            # we just check that we didn't exceed 2^numWeapons - 1 which represent all bits set to 1
            if top.weapons == (1 << numWeapons) - 1:
                return top.shots

            visited[top.weapons] = True

            for itm in range(0, m):
                # check first if we have visited this boss before
                if ((top.weapons >> itm) & 1) == 1:
                    pass

                best = bossHealth[itm]

                for itn in range(0, numWeapons):
                    if itm == itn:
                        pass

                    if ((top.weapons >> itn) & 1 == 1) and damageChart[itn][itm] != '0':
                        # we have weapons let's try it
                        harm = int(damageChart[itn][itm]) - int('0')
                        shots = math.floor(bossHealth[itm] / harm)
                        if bossHealth[itm] % harm != 0:
                            shots += 1
                        best = min(best, shots)

                heapq.heappush(pq, Node(top.weapons | (1 << itm), top.shots + best))
        return -1


#damageChart = ["198573618294842", "159819849819205", "698849290010992", "000000000000000", "139581938009384",
#               "158919111891911", "182731827381787", "135788359198718", "187587819218927", "185783759199192",
#               "857819038188122", "897387187472737", "159938981818247", "128974182773177", "135885818282838"]
#bossHealth = [157, 1984, 577, 3001, 2003, 2984, 5988, 190003, 9000, 102930, 5938, 1000000, 1000000, 5892, 38]

# damageChart = ["070", "500", "140"]
# bossHealth = [150, 150, 150]

damageChart = ["1542", "7935", "1139", "8882"]
bossHealth = [150, 150, 150, 150]
a = KiloManX()
print(a.leastShots(damageChart, bossHealth))
