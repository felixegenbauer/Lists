# Prime numbers
# Author: TODO: ???

import doctest


def primes(n):
    """
    Returns all prime numbers from 2 to n.

    :param n: the maximal number greater than 1
    :type n: int

    :return: list of prime numbers
    :rtype: list

    >>> primes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> max(primes(100))
    97
    >>> max(primes(1000))
    997
    >>> primes(0)
    []
    """

    return [0]


def is_prime(n):
    """
    Checks is given number is a prime number.

    :param n: number
    "type n: int

    :return: result

    >>> is_prime(-1)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(9)
    False
    >>> is_prime(997)
    True
    """
    return False


def factorise(n):
    """
    Finds prime factorisation of a given number.

    :param n: the number
    :type n: int

    :return: list of prime numbers
    :rtype: list

    >>> factorise(75)
    [3, 5, 5]
    >>> factorise(36)
    [2, 2, 3, 3]
    >>> factorise(1)
    []
    """

    return []


if __name__ == '__main__':
    doctest.testmod()
