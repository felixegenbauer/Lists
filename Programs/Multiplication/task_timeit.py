import time
import timeit
from functools import reduce
from operator import mul

# from task import product
from task_solution import product

from numpy import prod, array, arange
from numexpr import evaluate

# You may need to install some packages included above


# setting combinations of data and calculations

MAX_VALUE = 21

list_a = list(range(1, int(MAX_VALUE)))
list_b = array(list_a)
list_c = arange(1, MAX_VALUE, dtype=int)
list_d = arange(1, MAX_VALUE, dtype=float)


CONFIGURATIONS = [
    # using your function
    ["product(list_a)",
     "from __main__ import list_a, product"],
    # using reduce with a built-in operator
    ["reduce(mul, list_a)",
     "from __main__ import list_a, reduce, mul"],
    # using reduce with an anonymous lambda function, see Exercises/Lambda
    ["reduce(lambda x, y: x * y, list_a)",
     "from __main__ import list_a, reduce"],
    # using numpy
    ["prod(list_a)",
     "from __main__ import list_a, prod"],
    # using numexpr
    ["evaluate('prod(list_a)')",
     "from __main__ import list_a, evaluate"]
]

REPETITIONS = 1000 // MAX_VALUE

# warm up

t_end = time.time() + 1  # second(s) for warm up
while time.time() < t_end:
    res = time.time() + 3 ** .5  # just to keep CPU busy

# time comparisons

results = []
for d in ["a", "b", "c", "d"]:
    for [c, s] in CONFIGURATIONS:
        if d != "a":
            c = c.replace("list_a", "list_"+ d)
            s = s.replace("list_a", "list_" + d)

        t = timeit.timeit(c, setup=s, number=REPETITIONS)
        res = eval(c)
        results.append((t/REPETITIONS, d, c, res))


# sorting and displaying results

results.sort()

for r in results:
    print("{3:20d} {0:1.0g}\tlist_{1}\t{2}".format(r[0], r[1], r[2], int(r[3])))