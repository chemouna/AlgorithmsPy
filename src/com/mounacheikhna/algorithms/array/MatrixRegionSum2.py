
#
# +-----+-+-------+     +--------+-----+     +-----+---------+     +-----+--------+
# |     | |       |     |        |     |     |     |         |     |     |        |
# |     | |       |     |        |     |     |     |         |     |     |        |
# +-----+-+       |     +--------+     |     |     |         |     +-----+        |
# |     | |       |  =  |              |  +  |     |         |  -  |              |
# +-----+-+       |     |              |     +-----+         |     |              |
# |               |     |              |     |               |     |              |
# |               |     |              |     |               |     |              |
# +---------------+     +--------------+     +---------------+     +--------------+
#
#    sums[i][j]      =    sums[i-1][j]    +     sums[i][j-1]    -   sums[i-1][j-1]  + matrix[i-1][j-1]
#
# So, we use the same idea to find the specific area's sum.
#
# +---------------+   +--------------+   +---------------+   +--------------+   +--------------+
# |               |   |         |    |   |   |           |   |         |    |   |   |          |
# |   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
# |   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
# |   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
# |   |      |    |   |         |    |   |   |           |   |              |   |              |
# |   +------+    |   +---------+    |   +---+           |   |              |   |              |
# |        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
# +---------------+   +--------------+   +---------------+   +--------------+   +--------------+
#

class MatrixRegion:
    def __init__(self, matrix):
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.__sums = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # preprocessing
        # we start from 1 and leave the 0th index row and column with 0 values to remove
        # the edge cases checking
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                self.__sums[i][j] = self.__sums[i][j - 1] + matrix[i - 1][j - 1]

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                self.__sums[i][j] += self.__sums[i - 1][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.__sums[row2 + 1][col2 + 1] - self.__sums[row1][col2 + 1] \
               - self.__sums[row2 + 1][col1] + self.__sums[row1 + 1][col1 + 1]


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

matrixRegion = MatrixRegion(matrix)
print matrixRegion.sumRegion(0, 1, 2, 3)
print matrixRegion.sumRegion(1, 2, 3, 4)
