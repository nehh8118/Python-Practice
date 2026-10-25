'''Default dict
    similar to dictionary, but has a default value if value nto set yet
'''

from collections import defaultdict
d = defaultdict(int) #data type of default value
d['a'] = 1
d['b'] = 9
print(d)
print(d['c']) #will return 0 as c doesnt exsist in dictionary and type is int

de = defaultdict(list)
de['fruits'] = 'apple'
de['vegetable'] = 'carrot'
print(de)
print(de['juices'])