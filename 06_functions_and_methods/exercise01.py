# What happens when you run the following program? Why do we get that 
# result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)
# this produces a NameError because foo is not defined in the scope of 
# the main level - it is only defined within the function set_foo
