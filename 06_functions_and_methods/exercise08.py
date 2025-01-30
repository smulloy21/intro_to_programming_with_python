# Without running the following code, what do you think it will do?
def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)
# this will raise an error, because we are invoking foo with three 
# positional arguments, and it is only expecting (and will only 
# accept) two.
