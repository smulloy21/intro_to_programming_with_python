# Use a while loop to print all numbers in my_list with even values, 
# one number per line. Then, print the odd numbers using a ' for' loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    num = my_list[index]
    if num % 2 == 0:
        print(num)
    index += 1

for num in my_list:
    if num % 2 != 0:
        print(num)
