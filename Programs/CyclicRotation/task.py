# Cyclic Rotation
# Author: TODO: ???
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/


def solution(A, K):
    """
    Examples:
    >>> solution([3, 8, 9, 7, 6], 3)
    [9, 7, 6, 3, 8]
    >>> solution([0, 0, 0], 1)
    [0, 0, 0]
    >>> solution([1, 2, 3, 4], 4)
    [1, 2, 3, 4]
    >>> solution([], 2)
    []
    >>> solution([1, 2], 1)
    [2, 1]
    >>> solution([1, 2], 0)
    [1, 2]
    """
    counter=1
    newlist=A
    if len(A)!=0:
        while counter <= K:
            workinglist=[newlist[len(A)-1]]+newlist[:len(A)-1]
            newlist=workinglist
            counter=counter+1
    return newlist


if __name__ == '__main__':
    import doctest
    doctest.testmod()
