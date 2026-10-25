'''
product
    computes the cartesian product of input iterables. 
    To compute the product of an iterable with itself, use optional repeat keyword argument to specify the number of repetitions
    The output of this function is tuples in sorted order.
'''
from itertools import product

a = [1,2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

print(list(product(a, repeat=2)))
print(product(a, repeat=2)) #prints the iterator object

# print(list(product(['apple', 'banana'], 2))) #error as accepts iterables such as lists, tuples, and strings, but not standalone integers.
print(list(product(['apple', 'banana'], '2')))
print(list(product('AB', [2, 3])))