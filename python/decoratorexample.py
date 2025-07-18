#scope rewiew
s = 'Global Variable'

def check_for_locals():
    a=12
    print(locals())



def hello(name='Jose'):
    return 'Hello '+name

hello('pradeep')
hello()
hello
greet = hello
greet
greet()
del hello
hello()
greet()
#function within function
def hello(name='Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")
    hello()
    welcome()
#returning functions
def hello(name='Jose'):
    def greet():
        return '\t This is inside the greet() function'
    def welcome():
        return "\t This is inside the welcome() function"
    if name=='Jose':
        return greet
    else:
        return welcome
x=hello("ggh")
x
print(x())
#functions as arguments
def hello():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())

other(hello)

#creating a decorator
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()   
# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()