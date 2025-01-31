# Print all of the even numbers in the following list of nested lists. 
# This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

i = 0
while i < len(my_list):
    j = 0
    while j < len(my_list[i]):
        num = my_list[i][j]
        if num % 2 == 0:
            print(num)
        j += 1
    i += 1
