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
