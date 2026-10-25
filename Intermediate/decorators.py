'''
modify or extend teh beahvior of a function without changin its actual source
takes func as the arg
'''
def start_end_decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

def printName():
    print('Alex')

printName = start_end_decorator(printName)
printName()