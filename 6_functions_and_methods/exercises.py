# What happens when you run the following program? Why do we get that 
# result?

# def set_foo():
#     foo = 'bar'

# set_foo()
# print(foo)
# this produces a NameError because foo is not defined in the scope of 
# the main level - it is only defined within the function set_foo


# What does this program print? Why?
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
# this program prints bar, because at the main level where the print 
# statment is, foo is definied as the value 'bar' - foo only has the 
# value 'qux' within the set_foo function scope


# Identify the following items in that code:
# function name          multiply_numbers
# function arguments     2, 3, 4
# function definition    def multiply_numbers(num1, num2, num3):
#                            result = num1 * num2 * num3
#                            return result 
# function body          result = num1 * num2 * num3
#                        return result 
# function parameters    num1, num2, num3
# function invocation    multiply_numbers(2, 3, 4)
# function return value  24
# all identifiers        multiply_numbers, num1, num2, num3, result, product


# What does the following code print?
def scream(words):
    return words + '!!!!'

scream('Yipeee')
# this code prints nothing, because there is no call to `print`


# What does the following code print?
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')
# this code prints nothing, because there is no call to `print`.
# the code exits the function when it hits `return`, and never reaches
# the following line `print(words)`


# Without running the following code, what do you think it will do?
# def foo(bar, qux):
#     print(bar)
#     print(qux)

# foo('Hello') 
# this will throw an error, because we are trying to invoke the 
# function foo with the wrong number of arguments (and there is no 
# default argument defined)


# Without running the following code, what do you think it will do?
# def foo(bar, qux):
#     print(bar)
#     print(qux)

# foo(42, 3.141592, 2.718)
# this will raise an error, because we are invoking foo with three 
# positional arguments, and it is only expecting (and will only 
# accept) two.


# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)
# it will print 42, 3.141592, and 2.718 all on their own lines


# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)
# this will print 42, 3.141592, and 2 all on their own lines
# there is no third argument in the invokation of `foo`, but it has a
# default value that it will use instead


# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)
# this will print 42, 3, and 2, all on their own lines
# we invoke the function `foo` with only one argument, but that is ok
# because the second and third paramaters have default values


# Without running the following code, what do you think it will do?
# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo()
# this will throw an error, because we are trying to invoke the 
# function `foo` with no arguments. there are default values for
# the second and third parameters, but the first has no default and 
# therefore requires that we pass in an argument.


# Without running the following code, what do you think it will do?
# def foo(first, second=3, third):
#     print(first)
#     print(second)
#     print(third)

# foo(42)
# this will raise an error because we have a required argument 
# following a parameter with a default value. this is not allowed 
# in python


# Identify all of the identifiers on each line of the following code.
def multiply(left, right): # multiply, left, right
    return left * right # left, right

def get_num(prompt): # get_num, prompt
    return float(input(prompt)) # float, input, prompt

first_number = get_num('Enter the first number: ') # first_number, get_num
second_number = get_num('Enter the second number: ') # second_number, get_num
product = multiply(first_number, second_number) # product, multiply, first_number, second_number
print(f'{first_number} * {second_number} = {product}') # print, first_number, second_number, product


# Using the code below, classify the identifiers as global, local, or 
# built-in. For our purposes, you may assume this code is the entire 
# program.
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply: global
# left: local
# right: local
# get_num: global
# prompt: local
# float: built-in
# input: built-in
# first_number: global
# second_number: global
# product: global
# print: built-in


# In the code shown below, identify all of the function names and 
# parameters present in the code. Include the line numbers for each 
# item identified.
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# function names: multiply 184 192, get_num 187 190 191, float 188, input 188, print 193
# parameters: left 184 185, right 184 185, prompt 187 188 


# Which of the identifiers in the following program are function names? 
# Which are method names? Which are built-in functions?
def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))
# function names: say
# method names: upper, lower
# built-in functions: print, input, max


# The following function returns a list of the remainders of dividing 
# the numbers in numbers by 3:
def remainders_3(numbers):
    return [number % 3 for number in numbers]

# Use this function to determine which of the following lists contains 
# at least one number that is not evenly divisible by 3 (that is, the 
# remainder is not 0):
numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(any(remainders_3(numbers_1))) # True
print(any(remainders_3(numbers_2))) # True
print(any(remainders_3(numbers_3))) # False
print(any(remainders_3(numbers_4))) # False


# The following function returns a list of the remainders of dividing 
# the numbers in numbers by 5:
def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following lists do not 
# contain any numbers that are divisible by 5:
numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1))) # False
print(all(remainders_5(numbers_2))) # True
print(all(remainders_5(numbers_3))) # False
print(all(remainders_5(numbers_4))) # True
