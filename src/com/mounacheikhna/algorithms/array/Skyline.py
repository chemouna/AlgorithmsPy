class Skyline:
    def __init__(self):
        pass

    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        if not buildings:
            return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

        mid = (len(buildings) - 1) / 2
        left = self.getSkyline(buildings[0:mid + 1])
        right = self.getSkyline(buildings[mid + 1:])
        return self.merge(left, right)

    def merge(self, left, right):
        i = 0
        j = 0
        result = []
        h1 = None
        h2 = None
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                h1 = left[i][1]
                new = [left[i][0], max(h1, h2)]
                if result == [] or result[-1][1] != new[1]:
                    result.append(new)
                i += 1
            elif left[i][0] > right[j][0]:
                h2 = right[j][1]
                new = [right[j][0], max(h1, h2)]
                if result == [] or result[-1][1] != new[1]:
                    result.append(new)
                j += 1
            else:
                h1 = left[i][1]
                h2 = right[j][1]
                new = [right[j][0], max(h1, h2)]
                if result == [] or result[-1][1] != new[1]:
                    result.append([right[j][0], max(h1, h2)])
                i += 1
                j += 1
        while i < len(left):
            if result == [] or result[-1][1] != left[i][1]:
                result.append(left[i][:])
            i += 1
        while j < len(right):
            if result == [] or result[-1][1] != right[j][1]:
                result.append(right[j][:])
            j += 1

        return result


print Skyline().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
