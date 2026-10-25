'''named tuple
    immutable ds, acts like a regular tuple but can acces elements through dot notation
'''
from collections import namedtuple

Point = namedtuple('Point', 'x, y') 
#creates a class called point with x and y fields
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

student = namedtuple("student", ["name", "age", "dob"])
s1 = student("anna", 20, "12-09-1005")
print(s1.name) #dot notation
print(s1[0]) #accesing thru index


