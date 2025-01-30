# Without running the following code, what does it print? Why?
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113') # 'Product2' cause '113' is one of the match cases
bar_code_scanner(142) # 'Product not found!' cause the integer 142 is not 
                      # a match case, so it will go to the default
