# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)
# this will print 42, 3.141592, and 2 all on their own lines
# there is no third argument in the invokation of `foo`, but it has a
# default value that it will use instead
