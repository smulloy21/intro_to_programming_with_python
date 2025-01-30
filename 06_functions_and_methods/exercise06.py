# What does the following code print?
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')
# this code prints nothing, because there is no call to `print`.
# the code exits the function when it hits `return`, and never reaches
# the following line `print(words)`
