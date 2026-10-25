'''
groupby
    groups the elements based on the key or the lambda func given
'''
from itertools import groupby
def smaller_than_3(x):
    return x < 3

a=[1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3) #key= lambda x: x<3
for key, value in group_obj:
    print(key, value)
    print(key, list(value))

persons=[{'name': 'Tim', 'age': 25}, {'name': 'lisa', 'age': 25}, {'name': 'Dan', 'age': 75}]
group_obj1 = groupby(persons, key = lambda x: x['age'])
for key, value in group_obj1:
    print(key, list(value))