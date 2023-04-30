#!/usr/bin/python3
"""
You have n number of locked boxes in front of you./
Each box is numbered sequentially from 0 to n - 1 and/
each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List that contains all the boxes with the keys
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    openBox = {}
    while True:
        if len(openBox) == 0:
            openBox[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = None
        for box in openBox.items():
            if box.get('status') == 'opened':
                box['status'] = 'opened/checked'
                keys = box.get('keys')
        if keys:
            for key in keys:
                try:
                    if openBox.get(key) and openBox.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    openBox[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in openBox.values()]:
            continue
        elif len(openBox) == len(boxes):
            break
        else:
            return False

    return len(openBox) == len(boxes)


def main():
    """Summary"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()