'''
Decorator
    a function that is used to modify or extend the behavior of a function 
    without changin its actual source
    takes func as the arg(base func)
'''
import functools

'''basic decorator structure'''

def start_end_decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

@start_end_decorator #to add a decorator to func, add it bfore the function
def printName():
    print('Alex')

printName()

'''decorator with arguements'''

def decorator_with_args(func):

    @functools.wraps(func) #preserve info about used function
    def wrapper(*args, **kwargs): #can use arguments
        print(f"Calling {func.__name__} with args {args}")
        result = func(*args, **kwargs) #if not assigned to an variable, it returns none
        print(f"returned: {result}")
        return result #return the variable
    return wrapper

@decorator_with_args
def add(x, y):
    return x+y

result = add(10, 20)
print(result)

#print(help(add))
#print(add.__name__) function name

'''decorator that takes input: add extra nesting'''

def repeat(num_times): #accepts the decorator arg
    def decorator_repeat(func): #accepts the func
        def wrapper(*args, **kwargs): #accepts func arg
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # This will print the greeting 3 times

