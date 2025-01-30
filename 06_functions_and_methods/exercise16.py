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

# function names: multiply 4 12, get_num 7 10 11, float 8, input 8, print 13
# parameters: left 4 5, right 4 5, prompt 7 8 
