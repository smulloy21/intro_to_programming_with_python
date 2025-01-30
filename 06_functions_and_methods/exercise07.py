# Without running the following code, what do you think it will do?
def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello') 
# this will throw an error, because we are trying to invoke the 
# function foo with the wrong number of arguments (and there is no 
# default argument defined)
