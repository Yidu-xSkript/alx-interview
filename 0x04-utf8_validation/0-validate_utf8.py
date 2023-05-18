#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set
    represents a valid UTF-8 encoding.
    """

    encodingA = 1 << 7
    encodingB = 1 << 6
    bytes = 0

    for i in data:
        encodingByte = 1 << 7
        if bytes == 0:
            while encodingByte & i:
                bytes += 1
                encodingByte = encodingByte >> 1
            if bytes == 0:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if not (i & encodingA and not (i & encodingB)):
                    return False
        bytes -= 1
    if bytes == 0:
        return True
    return False