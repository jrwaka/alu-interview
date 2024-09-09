#!/usr/bin/python3

"""

Method that calculates the fewest number of operations
needed to result in exactly n 'H' characters in the file.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations required to achieve exactly 
    n 'H' characters in the file.
    
    :param n: The number of 'H' characters to achieve
    :type n: integer
    :return: The minimum number of operations
    """
    if n <= 1:
        return 0

    i = 2
    results = 0

    while i <= n:
        if n % i == 0:
            results += i
            n = n/i #or n //=i
        else:
            i += 1
    return results