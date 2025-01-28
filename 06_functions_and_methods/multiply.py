# Write a program that uses a multiply function to multiply two numbers 
# and returns the result. Ask the user to enter the two numbers, then 
# output the numbers and result as a simple equation.

# $ python multiply.py
# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128

def multiply(num1, num2):
    return num1 * num2

def get_number(prompt):
    number = input(prompt)
    return float(number)

num1 = get_number('Enter the first number: ')
num2 = get_number('Enter the second number: ')
product = multiply(num1, num2)
print(f'{num1} * {num2} = {product}')


# Consider this code:

def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)
