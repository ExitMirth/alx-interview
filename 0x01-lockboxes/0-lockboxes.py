def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    if not isinstance(boxes, list):
        return False

    if len(boxes) == 0:
        return False

    keys = [0]
    for key in keys:
        for box_index in boxes[key]:
            if box_index not in keys and 0 < box_index < len(boxes):
                keys.append(box_index)

    return len(keys) == len(boxes)
