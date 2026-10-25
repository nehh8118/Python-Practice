'''
accumulator
    takes two arg: iterable and function
    if no func is passed, addition is default
    does the operations for the elements and accumulates until element bfore it
'''
from itertools import accumulate
import operator

print(list(accumulate([1, 2, 3, 4]))) #[1, 3, 6, 10]
print(list(accumulate([1, 2, 3, 4], func=operator.mul)))
print(list(accumulate([1, 2, 3, 4, 3, 2], func=max)))

