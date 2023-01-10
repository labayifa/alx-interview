#!/usr/bin/python3
"""
pascal_triangle(n):  returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    res = []
    if type(n) != int or int(n) <= 0:
        return res
    else:
        for i in range(0, n):
            box = []
            for j in range(0, i + 1):
                box.append(triangle(i, j))
            res.append(box)
    return res


"""
    triangle(i, j): get the value at position i,j
"""


def triangle(i, j):
    if i == j or i <= 1 or j == 0:
        return 1
    elif j > i:
        return 0
    else:
        return triangle(i - 1, j - 1) + triangle(i - 1, j)
