#!/usr/bin/python3

def valid_utf8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes of data.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    bytes_to_follow = 0

    for byte in data:
        if bytes_to_follow == 0:
            if (byte >> 5) == 0b110:
                bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:
                bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_follow = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_to_follow -= 1

    return bytes_to_follow == 0


if __name__ == "__main__":
    # Test cases
    data = [65]
    print(valid_utf8(data))  # Output: True

    data = [80, 121, 116, 104, 111, 110, 32,
            105, 115, 32, 99, 111, 111, 108, 33]
    print(valid_utf8(data))  # Output: True

    data = [229, 65, 127, 256]
    print(valid_utf8(data))  # Output: False
