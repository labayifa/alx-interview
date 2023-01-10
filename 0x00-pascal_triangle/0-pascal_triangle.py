#!/usr/bin/python3

def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
        of integers representing the Pascal’s triangle of n
    """
    res = []
    if type(n) != int or int(n) <= 0:
        return res
    else:
        for i in range(1, n + 1):
            box = []
            data = 1
            for j in range(1, i + 1):
                box.append(data)
                data = data * (i - j) // j
            res.append(box)
    return res
