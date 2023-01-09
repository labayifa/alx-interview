#!/usr/bin/python3
"""
    canUnlockAll: Take a list of list and determine if can unlock all boxes.
"""


def canUnlockAll(boxes):
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
