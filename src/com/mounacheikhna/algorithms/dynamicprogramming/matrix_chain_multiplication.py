import sys


def chain_matrix_multiplication(matrices, i, j):
    if i == j:
        return 0

    cMin = sys.maxsize
    for k in range(i, j):
        count = chain_matrix_multiplication(matrices, i, k) + chain_matrix_multiplication(matrices, k + 1, j) + (
            matrices[i - 1] * matrices[k] * matrices[j])

        if count < cMin:
            cMin = count

        k += 1
    return cMin


arr = [1, 2, 3, 4, 3]
print(chain_matrix_multiplication(arr, 1, len(arr) - 1))


def matrix(m, n):
    return [[0] * n for _ in range(m)]


# def matrix_chain(p):
#     n = len(p) - 1
#     T = matrix(n, n)
#     S = matrix(n, n)


# @param p: an array of numbers, where p[i] represents a side length of a matrix
# example: [1, 2, 3] represents a 1 x 2 and 2 x 3 matrix, in that order
# @return: the minimum number of operations it would take to multiply the
# sequence of matrices most efficiently
def matrix_chain_order(p):
    n = len(p) - 1  # number of matrices in input
    costs = [[0 for _ in range(n)] for _ in range(n)]  # an empty nxn cost matrix
    # length: number of matrices to consider
    for length in range(2, n + 1):  # start from 2 because we dont need to calculate multiplication for one matrix
        # since its 0 (default value)
        # i: the 0-index of the matrix
        for i in range(n - length + 1):
            # j: the 0-index of the j matrix
            j = i + length - 1
            costs[i][j] = float('inf')
            # k: the 0-index of the matrix whose right edge is considered
            # the k. Note: this is not the same as the actual index to
            # the right edge (which is k + 1).
            for k in range(i, j):
                possible_cost = costs[i][k] + costs[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                costs[i][j] = min(costs[i][j], possible_cost)
    return costs[0][n - 1]

print(matrix_chain_order(arr))
