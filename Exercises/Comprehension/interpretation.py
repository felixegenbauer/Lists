"""
>>> [x**2 for x in range(5)]
[]  # TODO complete the test before running it

>>> [word[0] for word in ["this","is","a","list","of","words"] ]
[]  # TODO complete the test before running it

>>> [x.lower() for x in ["A","B","C"]]
[]  # TODO complete the test before running it

>>> [x for x in "Hello 12345 World" if x.isdigit()]
[]  # TODO complete the test before running it

>>> [len(x) for x in "the quick brown fox jumps over the lazy dog".split()]
[]  # TODO complete the test before running it
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()

