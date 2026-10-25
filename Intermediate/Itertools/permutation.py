'''
permutation
    generates all possible permuations of an iterable
    the iterable and the grp size as args
    groupd size is the len of the iterable by default if not mentioned
'''
from itertools import permutations

print(list(permutations([1, 2, 3])))
print(list(permutations([1, 2, 3], 2)))
print(list(permutations('ab')))
print(list(permutations(range(3), 2)))
