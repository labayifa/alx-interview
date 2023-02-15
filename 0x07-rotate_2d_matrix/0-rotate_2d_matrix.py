#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    :param matrix:
    :return:
    """
    n = len(matrix)
    matrixRes = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix[n - i - 1][j])
        matrixRes.append(row)

    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrixRes[i][j]
