def euler81(grid):
    sums = grid
    for i in reversed(range(len(grid))):
        for j in reversed(range(len(grid[i]))):
            if i + 1 < len(grid) and j + 1 < len(grid[i]):
                temp = min(grid[i + 1][j], grid[i][j + 1])
            elif i + 1 < len(grid):
                temp = grid[i + 1][j]
            elif j + 1 < len(grid[i]):
                temp = grid[i][j + 1]
            else:
                temp = 0
            sums[i][j] += temp
    return str(sums[0][0])


grid = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]

if __name__ == "__main__":
    print euler81(grid)
