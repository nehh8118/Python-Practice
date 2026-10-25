'''Counter
    counter is a container that stores elements as 
    dictionary keys and thier count as values
'''
from collections import Counter

a = 'ccccbbbbbaaa'
myCounter=Counter(a)
print(myCounter)
print("Keys:", myCounter.keys())
print("Values:", myCounter.values())
print("Most common element:", myCounter.most_common(3)[0][0]) #o/p: [('b', 5), ('c', 4), ('a', 3)] 
#as it gives a tuple of most common n elements, accessing first tuple, then element of that tuple

print("List of distinct elements:", list(myCounter))
print("List of all elements:", list(myCounter.elements()))
