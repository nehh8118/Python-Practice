'''Deque
    move elements from both ends
'''
from collections import deque

d = deque()

d.append(1)
d.append(2)
d.pop() 
d.extend([3, 4, 5]) #operations to the right

d.appendleft(3)
print(d)
d.popleft()
print(d)
d.extendleft(9, 7) #operaation to the left

d.rotate(1) #rotate k elements to the right
d.rotate(-1) #rotate k elements to the left, negative num
print(d)

d.clear()
print(d)