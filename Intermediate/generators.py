'''
Generators
    func that return an object that can be iterated over
    creates iterators that generate values on the fly(lazy evaluation)
        intead of computing them all at once
    memory efficient
    uses yield over return
        yield: pauses the function, saves all internal state(variables, loops etc)
        and hands a value back to caller, when called again, it starts from where it left
'''
def count_upto(limit):
    count=1
    while count <= limit:
        yield count
        count+=1

counter = count_upto(3) #generator object
print(counter)

print(next(counter)) #use for loop or next() to access output
print(next(counter))

'''usage: If you attempt to read a multi-gigabyte log file using file.readlines(), 
Python loads the entire file into RAM, threatening to crash your system.
 A generator streams the file line-by-line seamlessly'''

