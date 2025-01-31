# Which of the following values can't be used as a key in a dict 
# object, and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b'] # NO
{'a': 1, 'b': 2} # NO
range(5)
{1, 4, 9, 16, 25} # NO
3
0.0
frozenset({1, 4, 9, 16, 25})

# lists, sets, and dicts cannot be keys in a dict because they are 
# mutable and therefore unhashable
