# How would you print all the numbers in the following range?
r = range(3, 17, 4)

print(list(r))
# Since ranges are lazy sequences, we must either iterate over the 
# range or convert the range to a non-lazy sequence like a list
