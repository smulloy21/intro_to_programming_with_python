# Without running the following code, what do you think it will do?
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
# this will raise an error because we have a required argument 
# following a parameter with a default value. this is not allowed 
# in python
