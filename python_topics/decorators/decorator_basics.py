from datetime import datetime
from functools import wraps

# 1. a function is an object, because of that it can be assigned to a variable

def my_function():
    print("I am a function.")

description = my_function
print(description())

# 2. a function can be nested inside another function

def outer_function():
    def inner_function():
        print('I came from the inner function')
    inner_function()

outer_function()


# 3. A function can be also be returned by another function

def outer_function():
    task = 'Read python book'
    def inner_function():
        print(task)
    return inner_function

homework = outer_function()
homework()

# 4. a function can be passed to another function as an argument

def friendly_reminder(func):
    func()
    print('Don\'t forget to get your wallet!')

def action():
    print('I am going to the store to buy u something nice.')

friendly_reminder(action)

# creating a python decorator
# 1. create an outer function that takes function as an argument
# 2. there is also an inner function that wraps around the decorated function

def my_decorator_func(func):
    def wrapper_func():
        # do something before the func
        func()
        # do something after the func
    return wrapper_func

# to use this decorator, do it like below
@my_decorator_func
def my_func():
    pass


# example decorator to log date and time a function is executed

def log_datetime(func):

    def wrapper():
        print(f'Function: {func.__name__}\n run on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper

@log_datetime
def daily_backup():
    print('Daily backup job has finished')

daily_backup()

# adding arguments to decorators in python
# *args will take unlimited number of arguments of any type
# **kwargs will take unlimited number of keyword arguments 

# here is a decorator with arguments

def my_decorator_func(func):
    def wrapper_func(*args, **kwargs):
        # do something before
        func(*args, **kwargs)
        # do something after
    return wrapper_func

@my_decorator_func
def my_func(my_arg):
    pass

# decorators hide the function they are decorating
# to fix this use functools. functools wraps will update the decorator with the 
# decorated function attributes

def my_decorator_func1(func):

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func

@my_decorator_func1
def my_func1(my_args):
    pass







