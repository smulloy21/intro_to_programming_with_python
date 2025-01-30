# This question may be a little challenging if your math skills are 
# rusty. Don't be afraid to take advantage of the hints. Try your best 
# to solve the problem, but don't feel compelled to complete it if you 
# become frustrated.

# Use the REPL and the arithmetic operators to extract the individual 
# digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.
# Each digit may require multiple Python statements.
num = 4936
ones_digit = num % 10
tens_digit = num % 100 // 10
hundreds_digit = num % 1000 // 100
thousands_digit = num % 10000 // 1000
print(f'{thousands_digit} {hundreds_digit} {tens_digit} {ones_digit}')
