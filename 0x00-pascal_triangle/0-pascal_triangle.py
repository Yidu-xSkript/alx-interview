#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of
    lists of integers representing the Pascal's triangle of n
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            current = 1
            for j in range(1, i + 1):
                level.append(current)
                current = current * (i - j) // j
            triangle.append(level)
    return triangle