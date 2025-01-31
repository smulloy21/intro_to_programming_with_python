# Modify the age.py program you wrote in Exercise 3 of the Input/Output 
# chapter. The updated code should use a for loop to display the future 
# ages.

# Write a program named that asks the user to enter their age, 
# then calculates and reports the future age 10, 20, 30, and 40 years 
# from now. Here's the output for someone who is 27 years old.

# How old are you? 27

# You are 27 years old.
# In 10 years, you will be 37 years old.
# In 20 years, you will be 47 years old.
# In 30 years, you will be 57 years old.
# In 40 years, you will be 67 years old.

age = int(input('How old are you? '))

print()
print(f'You are {age} years old.')

for year in range(10, 50, 10):
    print(f'In {year} years, you will be {age + year} old.')
