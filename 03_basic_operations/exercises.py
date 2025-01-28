# concatenate two strings
first_name = 'Jane'
last_name = 'Doe'
full_name = f'{first_name} {last_name}'
print(full_name)


# extract individual digits of 4936
num = 4936
ones_digit = num % 10
tens_digit = num % 100 // 10
hundreds_digit = num % 1000 // 100
thousands_digit = num % 10000 // 1000
print(f'{thousands_digit} {hundreds_digit} {tens_digit} {ones_digit}')


# what does `print('5' + '10') do? why?`
print('5' + '10') # 510
# this concatenates the two numbers as strings
# if integer addition is desired, the numbers must be integers
print(5 + 10) # 15


# will an error occur if you try to access a list element 
# with an index out of range?
foo = ['a', 'b', 'c']
# print(foo[3]) # will this result in an error?
# yes, it results in an out of range index error


# what value does the following expression evaluate?
print('foo' == 'Foo')
# this is False, because string comparison is case sensitive


# what will the following code do? why?
# print(int('3.1415'))
# this code raises a ValueError because the string to be coerced to an int 
# is not base 10 (i.e. it's a float string, not an integer string or a float)


# to what value does the following expression evaluate?
print('12' < '9') # True
# this evaluates to True, because it compares the two values as strings, and
# '1' < '9' (string evaluation compares the values character by character)
