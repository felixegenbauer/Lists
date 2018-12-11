# Demonstration of reflection mechanisms
# Author: Joanna Chimiak-Opoka

import inspect  # module with more reflection-enabling functions
import sys

import string as module  # TODO: change to another module if you wish


def print_list(a_list, a_type, a_module_name):
    """
    Prints information about a given list and the list itself.
    Additionally, it prints some reflection information.

    :param a_list: list to print
    :param a_type: category of elements in the list
    :param a_module_name: name of the module, the list is from
    :return: nothing, it is printing function
    """

    # functional part ----------------------------------------------------------

    print("-"*3, "functional part:")
    print(len(a_list),
          "{} in {} package\n".format(a_type, a_module_name) +
          "\n".join(a_list))

    # reflective part ----------------------------------------------------------

    # accessing reflective information

    module_name = __name__
    frame_current = inspect.currentframe()
    filename = inspect.getframeinfo(frame_current).filename

    function_name = inspect.getframeinfo(frame_current).function
    function_object = getattr(sys.modules[__name__], function_name)
    function_signature = inspect.signature(function_object)

    args, _, _, values = inspect.getargvalues(frame_current)

    # presenting reflective information

    print("-"*3, " reflective part:")
    print("printed by " + module_name + "." + function_name + str(function_signature))
    print("\tdefined in " + filename)
    print("\tcalled with arguments:", end="")
    print(" ".join(["\n\t\t%s = %s : %s" % (arg, values[arg], type(values[arg]).__name__) for arg in args]))
    print("-" * 10)
    print()


if __name__ == '__main__':

    # reflective information about the module ----------------------------------

    # objects of the imported module
    #     sorted ignoring cases and leading underscores

    objects = sorted(dir(module),
                     key=lambda x: x[:2] == "__" and x[2:].lower() or x[0] == "_" and x[1:].lower() or x.lower())

    # presenting all objects

    print_list(objects, "objects ", module.__name__)

    # filtered lists of objects, only "public" based on naming convention
    #     two lines of code below are doing the same thing with different methods
    #     1) filter() with anonymous function
    #     2) list comprehension

    print_list(list(filter(lambda x: x[0] != "_", objects)), "public objects", module.__name__)

    print_list([x for x in objects if x[0] != "_"], "public objects", module.__name__)

    # TODO: show "private" objects only, e.g. "_string"

    # TODO: show "magic" objects only, e.g."__doc__"

    # to show public methods / functions one has to check if a object is callable

    print_list([x for x in objects if x[0] != "_" and callable(getattr(module, x))],
               "public functions", module.__name__)

    # TODO: show only magic attributes / variables

    # reflective part about __main__ -------------------------------------------

    module_current = sys.modules[__name__]

    print("-"*10)
    print("end of " + __name__ + " containing:", end="")
    print(" ".join(["\n%s: %s" %
                    (i, type(getattr(module_current, i)).__name__)
                    for i in dir(module_current)]))
    print("-" * 10)
    print()
