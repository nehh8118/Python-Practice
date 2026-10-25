'''
combination
    generates all possible combinations of an iterable
    in sorted order
    groupd size is the len of the iterable by default if not mentioned
'''

from itertools import combinations, combinations_with_replacement
a=[1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr)) #makes combinations with itself