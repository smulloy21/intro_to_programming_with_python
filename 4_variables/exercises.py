# classify the following variable names as idiomatic, non-idomatic, or 
# illegal. explain why.
# index # idiomatic
# CatName # non-idiomatic, except as a class name. should be snake_case
# lazy_dog # idiomatic
# quick_Fox # non-idiomatic, should use lowercase only
# 1stCharacter # illegal; should not begin with a digit
# operand2 # idiomatic
# BIG_NUMBER # non-idiomatic, except as a constant. should be lowercase
# π # non-idiomatic. should be ASCII-only


# classify the following function names as idiomatic, non-idiomatic, or 
# illegal. explain why.
# index # idiomatic
# CatName # non-idiomatic. should be snake_case
# lazy_dog # idiomatic
# quick_Fox # non-idiomatic. should be all lowercase
# 1stCharacter # illegal. cannot start with a digit
# operand2 # idiomatic
# BIG_NUMBER # non-idiomatic. should be all lowercase
# π # non-idiomatic. should be ASCII-only


# classify the following constant names as idiomatic, non-idiomatic, or 
# illegal. explain why.
# index # non-idiomatic. should be all uppercase
# CatName # non-idiomatic. should be all uppercase, with an underscore between words
# snake_case # non-idiomatic. should be all uppercase for constant names
# LAZY_DOG3 # idiomatic
# 1ST # illegal. cannot start with a digit
# operand2 # non-idiomatic. should be all uppercase
# BIG_NUMBER # idiomatic
# Π # non-idiomatic. should be ASCII-only


# classify the following class names as idiomatic, non-idiomatic, or 
# illegal. explain why.
# index # non-idiomatic. should begin with an uppercase letter
# CatName # idiomatic
# Lazy_Dog # non-idiomatic. should not have any underscores
# 1ST # illegal. should not begin with a digit
# operand2 # non-idiomatic. should begin with an uppercase letter
# BigNumber3 # idiomatic
# Πi # non-idiomatic. should be ASCII-only characters


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


# Assume you have $1,000.00 in the bank, and you've somehow managed to 
# find a bank that pays you 5% (this is a wish-fulfillment fantasy) 
# compounded interest every year. After one year, you will have $1,050 
# ($1,000 times 1.05). After two years, you will have $1,050 times 
# 1.05, or $1102.50. Create a variable named balance that contains the 
# amount of money you will have after 5 years, then print the result. 
# Use a single expression if you can to set balance to the correct 
# value.

initial_amount = 1000
years = 5
balance = initial_amount * (1.05**years)

print(f'After {years} years, the balance is ${balance:,.2f}.')


# Repeat the previous question but, this time, use augmented 
# assignment to compute the final result, one year at a time.

amount = 1000
years = 5
amount *= 1.05**years

print(f'After {years} years, the balance is ${amount:,.2f}.')


# Assume that obj already has a value of 42 when the code below starts 
# running. Which of the subsequent statements reassign the variable? 
# Which statements mutate the value of the object that obj references? 
# Which statements do neither? If necessary, you can read the 
# documentation.

obj = 'ABcd' # reassigns
obj.upper() # neither - new value is returned
obj = obj.lower() # reassigns - strings are immutable
print(len(obj)) # neither
obj = list(obj) # reassigns
obj.pop() # mutates
obj[2] = 'X' # mutates
obj.sort() # mutates
set(obj) # neither - new value, unassigned
obj = tuple(obj) # reassigns

print(obj) # ('X', 'a', 'b')
