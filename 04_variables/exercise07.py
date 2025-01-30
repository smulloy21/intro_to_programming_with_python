# What happens when you run the following code? Why?
NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)
# This code greets Victor three times, then greets Nina three times. 
# Even though the name variable is a constant, it is still mutable. 
# Python doesn't have real constants, just an all caps convention for 
# variables that should be treated as constant.
