# Write a function that computes and returns the factorial of a number 
# by using a for or while loop. The factorial of a positive integer n, 
# signified by n!, is defined as the product of all integers between 1 
# and n, inclusive:

# n!	Expansion	        Result
# 1!	1	                1
# 2!	1 * 2	            2
# 3!	1 * 2 * 3	        6
# 4!	1 * 2 * 3 * 4	    24
# 5!	1 * 2 * 3 * 4 * 5   120

# You may assume that the argument is always a positive integer.

def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result

print(factorial(5)) # 120
