#!/usr/bin/python3
"""In a text file, there is a single character H.
our text editor can execute only two operations
in this file: Copy All and Paste. Given a number
n, write a method that calculates the fewest number
of operations needed to result in exactly n H
characters in the file."""


def minOperations(n):
    """ The method that results in the above statement"""

    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops