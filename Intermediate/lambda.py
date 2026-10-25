# lambda arg: expression
# does the same thing as functions but uses way less lines of code
from functools import reduce

add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x*y
print(mult(2, 7))

point = [(1, 2), (15, 1), (5, -1), (10, 4)]
print(point)
print(sorted(point)) #by default, sorts on the basis of first element
using_lambda = sorted(point, key = lambda x:x[1]) #now sorts on basis of second element
print(using_lambda)

# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a) #maps the function for each element in the list
print(list(b))

# filter(func, seq)
c = [1, 2, 3, 4, 5, 6]
d = filter(lambda x: x%2==0, c) #to get just the even nums
print(list(d))

# reduce(func, seq)
prod = reduce(lambda x, y: x*y, c) #apply function an reduce to one element, i think it gives the last element in list after accumulate
print(prod)


