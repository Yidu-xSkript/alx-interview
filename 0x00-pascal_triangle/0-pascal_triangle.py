#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle of n
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            curr = 1
            for j in range(1, i + 1):
                level.append(curr)
                curr = curr * (i - j) // j
            triangle.append(level)
    return triangle