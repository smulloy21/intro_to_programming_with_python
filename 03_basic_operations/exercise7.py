# What will the following code do? Why?
int('3.1415')
# this code raises a ValueError because the string to be coerced to an int 
# is not base 10 (i.e. it's a float string, not an integer string or a float)
