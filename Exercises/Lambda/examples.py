# --- basic examples -----------------------------------------------------------

print("basic example with one argument:", end=" ")


def absolute(x):
    # definition of a (named) function...
    return x > 0 and x or -x


# ...and its invocation

res = absolute(-2)
print(res, end=" ")

res = absolute(2)
print(res, end=" ")

# definition of anonymous function and its invocation

res = (lambda x: x > 0 and x or -x)(-2)
print(res, end=" ")

res = (lambda x: x > 0 and x or -x)(2)
print(res)


print("basic example with two arguments:", end=" ")


def add(x, y):
    # definition of a (named) function...
    return x + y


# ...and its invocation

res = add(2, 3)
print(res, end=" ")

# definition of anonymous function and its invocation

res = (lambda x, y: x + y)(2, 3)
print(res)


# --- usage examples -----------------------------------------------------------

# in sort(), which is the most popular usage
print("usage example with sort():")


student_data = [['john', 3, 90], ['jane', 2, 50], ['dave', 3, 60]]  # name, semesters, credits

res = sorted(student_data, key=lambda student: -student[2])   # sort by credits descending
print(res)

res = sorted(student_data, key=lambda student: -student[2]/student[1])   # sort by studying pace descending
print(res)

# in filter() and map() with single argument

res = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print("usage example with filter():", list(res))

res = map(lambda x: x**2, [1, 2, 3, 4])
print("usage example with map():", list(res))

# in map() with two arguments

res = map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30])
print("usage example with map():", list(res))
