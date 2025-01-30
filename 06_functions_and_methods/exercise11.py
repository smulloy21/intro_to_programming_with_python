# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)
# this will print 42, 3, and 2, all on their own lines
# we invoke the function `foo` with only one argument, but that is ok
# because the second and third paramaters have default values
