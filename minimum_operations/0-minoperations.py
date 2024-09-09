#!/usr/bin/python3

"""Method that calculates the fewest number of operations
needed to result in exactly n H characters in the file."""

def minOperations(n):
    """Minimum Operations"""

    if n <= 1:
        return 0

    i = 2
    results = 0

    while i <= n:
        if n % i == 0:
            results += i
            n = n/i
        else:
            i += 1
    return results