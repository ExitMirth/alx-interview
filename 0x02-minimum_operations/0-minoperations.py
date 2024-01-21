#!/usr/bin/python3
"""
Minimum Operations module
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters.

    Args:
        n (int): Number of H characters to achieve.

    Returns:
        int: Fewest number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format
          (n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format
          (n, minOperations(n)))
