from itertools import count, cycle, repeat

for i in count(14): #will count infinitely from start value given
    print(i) 
    if i==15: #to stop
        break

a = [1, 2, 3]
for i in cycle(a): #cycle infinitely thru an iterable
    print(i)
    break

for i in repeat(1, 4):
    print(i)
