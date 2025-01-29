# To what values do the following expressions evaluate?
False or (True and False)   # False
True or (1 + 2)             # True
(1 + 2) or True             # 3
True and (1 + 2)            # 3
False and (1 + 2)           # False
(1 + 2) and True            # True
(32 * 4) >= 129             # False
False != (not True)         # False
True == 4                   # False
False == (847 == '847')     # True


# Write a function, even_or_odd, that determines whether its argument 
# is an even or odd number. If it's even, the function should print 
# 'even'; otherwise, it should print 'odd'. Assume the argument is 
# always an integer.
def even_or_odd(num):
    print('even' if num % 2 == 0 else 'odd')


# Without running the following code, what does it print? Why?
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113') # 'Product2' cause '113' is one of the match cases
bar_code_scanner(142) # 'Product not found!' cause the integer 142 is not 
                      # a match case, so it will go to the default


# Refactor this statement to use a regular if statement instead.
# return ('bar' if foo() else qux())

# if foo():
#     return 'bar'
# else: 
#     return qux()


# What does this code output, and why?
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([]) # 'Empty' cause an empty list is falsy, so it evaluates the 
                  # `else` block


# Write a function that takes a string as an argument and returns an 
# all-caps version of the string when the string is longer than 10 
# characters. Otherwise, it should return the original string. Example: 
# change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.
def caps_long(string):
    return string.upper() if len(string) > 10 else string

print(caps_long('hello world'))
print(caps_long('goodbye'))


# Write a function that takes a single integer argument and prints a message 
# that describes whether:
# - the value is between 0 and 50 (inclusive)
# - the value is between 51 and 100 (inclusive)
# - the value is greater than 100
# - the value is less than 0

def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0
