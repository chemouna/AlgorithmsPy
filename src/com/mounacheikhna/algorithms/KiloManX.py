import heapq
import math


class Node(object):
    def __init__(self, weapon, shots):
        self.weapon = weapon
        self.shots = shots

    def __lt__(self, other):
        return self.shots < other.shots


class KiloManX:
    def leastShots(self, damageChart, bossHealth):
        pq = []
        visited = []
        top = Node(0, 0)
        heapq.heappush(pq, top)

        m = len(damageChart)
        numWeapons = len(damageChart[0])
        for i in range(1 << 15):
            visited.append(False)

        while pq:
            top = heapq.heappop(pq)

            # make sure we dont visit the same configuration twice
            if visited[top.weapon]:
                pass

            visited[top.weapon] = True

            # To check if we have all the weapons which means we defeated all bosses
            # we just check that we didn't exceed 2^numWeapons - 1 which represent all bits set to 1
            if top.weapon == (1 << numWeapons) - 1:
                return top.shots

            for itm in range(0, m):
                # check first if we have visited this boss before
                if top.weapon >> itm & 1: # why this ?
                    continue

                best = bossHealth[itm]
                for itn in range(0, m):
                    if itm == itn:
                        pass

                    if ((top.weapon >> itm) & 1 == 1) and damageChart[itn][itm] != '0':
                        # we have a weapon let's try it
                        harm = (damageChart[itn][itm] - '0')
                        shots = math.floor(bossHealth[itm] / harm)
                        if bossHealth[itm] % harm != 0:
                            shots += 1
                        best = min(best, shots)

                heapq.heappush(pq, Node(top.weapon | (1 << itm), top.shots + best)) # ??
        return -1


#damageChart = ["198573618294842", "159819849819205", "698849290010992", "000000000000000", "139581938009384",
#               "158919111891911", "182731827381787", "135788359198718", "187587819218927", "185783759199192",
#               "857819038188122", "897387187472737", "159938981818247", "128974182773177", "135885818282838"]
#bossHealth = [157, 1984, 577, 3001, 2003, 2984, 5988, 190003, 9000, 102930, 5938, 1000000, 1000000, 5892, 38]
damageChart = ["1542", "7935", "1139", "8882"]
bossHealth = [150, 150, 150, 150]
a = KiloManX()
print(a.leastShots(damageChart, bossHealth))
