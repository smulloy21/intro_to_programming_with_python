my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:
# 1. Are the lists assigned to my_list and another_list equal?
# 2. Are the lists assigned to my_list and another_list the same object?
# 3. Are the nested lists at index 3 of my_list and another_list equal?
# 4. Are the nested lists at index 3 of my_list and another_list the same object?

# 1. yes, they will evaluate to equal using the == operator, they have the 
# same values
# 2. the two lists are not the same object, they are different objects. the 
# list constructor makes a new object
# 3. yes, the nested lists at index 3 are equal, they have the same values
# 4. yes, the nested lists at index 3 are the same object. that is because 
# the list constructor performs a shallow copy, which does not include nested 
# collections, just the reference to them
