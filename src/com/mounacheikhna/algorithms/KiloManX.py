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

            for i in range(0, m):
                # check first if we have visited this boss before
                if top.weapon >> i & 1: # why this ?
                    continue

                best = bossHealth[i]
                for j in range(0, m):
                    if i == j:
                        continue

                    if top.weapon >> i && damageChart[j][i] != '0':
                        # we have a weapon let's try it
                        shotsNeeded = bossHealth[i] / (damageChart[j][i] - '0') # why here too ?
                        if bossHealth[i] % (damageChart[j][i] - '0') != 0:
                            shotsNeeded += 1
                        best = min(best, shotsNeeded)

                heapq.heappush(pq, Node(top.weapon | (1 << i), top.shots + best)) # ??

damageChart = ["198573618294842", "159819849819205", "698849290010992", "000000000000000", "139581938009384",
               "158919111891911", "182731827381787", "135788359198718", "187587819218927", "185783759199192",
               "857819038188122", "897387187472737", "159938981818247", "128974182773177", "135885818282838"]
bossHealth = [157, 1984, 577, 3001, 2003, 2984, 5988, 190003, 9000, 102930, 5938, 1000000, 1000000, 5892, 38]
# damageChart = ["1542", "7935", "1139", "8882"]
# bossHealth = [150,150,150,150]
a = KiloManX()
print(a.leastShots(damageChart, bossHealth))
