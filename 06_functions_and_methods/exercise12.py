# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()
# this will throw an error, because we are trying to invoke the 
# function `foo` with no arguments. there are default values for
# the second and third parameters, but the first has no default and 
# therefore requires that we pass in an argument.
