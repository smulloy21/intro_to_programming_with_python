# What does this program print? Why?
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
# this program prints bar, because at the main level where the print 
# statment is, foo is definied as the value 'bar' - foo only has the 
# value 'qux' within the set_foo function scope
