def precomputeSums(matrix):
    top_row, bottom_row = (0, len(matrix) - 1)
    left_col, right_col = (0, len(matrix[0]) - 1)

    sums = [[0] * (right_col - left_col + 1) for i in range(bottom_row - top_row + 1)]
    sums[top_row][left_col] = matrix[top_row][left_col]

    for col in range(left_col + 1, right_col + 1):
        sums[top_row][col] = sums[top_row][col - 1] + matrix[top_row][col]

    for row in range(top_row + 1, bottom_row + 1):
        sums[row][left_col] = sums[row - 1][left_col] + matrix[row][left_col]

    for col in range(left_col + 1, right_col + 1):
        columnSum = matrix[top_row][col]
        for row in range(top_row + 1, bottom_row + 1):
            sums[row][col] = sums[row][col - 1] + matrix[row][col] + columnSum
            columnSum += matrix[row][col]

    return sums


def matrixRegionSum(matrix, A, D, sums):
    if len(matrix) == 0:
        return
    if A[0] == 0 or A[1]:
        OA = 0
    else:
        OA = sums[A[0] - 1][A[1] - 1]

    if A[1] == 0:
        OC = 0
    else:
        OC = sums[D[0]][A[1] - 1]

    if A[0] == 0:
        OB = 0
    else:
        OB = sums[A[0] - 1][D[1]]

    OD = sums[D[0]][D[1]]

    return OD - OB - OC + OA

