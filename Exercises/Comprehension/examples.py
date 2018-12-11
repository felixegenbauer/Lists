# List Comprehension

# --- setting an initial list --------------------------------------------------

number = 5
list_initial = list(range(number, 3 * number))
print(list_initial)

# --- loop and list comprehension equivalents ----------------------------------

# --- for loop example:

list_new = []
for e in list_initial:
    if e > 2 * number:
        list_new.append(e * number)
print(list_new)

# --- list comprehension equivalent:

list_new = [e * number for e in list_initial if e > 2 * number]
print(list_new)


# --- more generic form of the above -------------------------------------------

# the same examples, but with invocations of functions
# to easily see the corresponding parts of both notations

def my_expression(item):
    return item * number


def my_filter(item):
    return item > 2 * number


# --- for loop example:

list_new = []
for e in list_initial:
    if my_filter(e):
        list_new.append(my_expression(e))
print(list_new)

# --- list comprehension equivalent:

list_new = [my_expression(e) for e in list_initial if my_filter(e)]
print(list_new)
