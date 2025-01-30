# What does this code output, and why?
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([]) # 'Empty' cause an empty list is falsy, so it evaluates the 
                  # `else` block
