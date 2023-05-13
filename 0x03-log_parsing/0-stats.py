#!/usr/bin/python3

import sys


def logParser(statusCode, fileSize):
    """
    Method to print
    Args:
        statusCode: status code (200, 301, ...)
        fileSize: total file size
    Return: void
    """

    print("File size: {}".format(fileSize))
    for key, val in sorted(statusCode.items()):
        if val != 0:
            print("{}: {}".format(key, val))


status_code = {"200": 0, "301": 0, "400": 0,
               "401": 0, "403": 0, "404": 0,
               "405": 0, "500": 0}
fileSize = 0
i = 0


try:
    for line in sys.stdin:
        _line = line.split()
        _line = _line[::-1]

        if len(_line) > 2:
            i += 1

            if i <= 10:
                fileSize += int(_line[0])
                state = _line[1]

                if (state in status_code.keys()):
                    status_code[state] += 1

            if (i == 10):
                logParser(status_code, fileSize)
                i = 0

finally:
    logParser(status_code, fileSize)
