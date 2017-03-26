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
n = len(arr)
print(chain_matrix_multiplication(arr, 1, n - 1))
