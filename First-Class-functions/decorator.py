from functools import wraps
# Decorators


def decorator_func(original_function):
    def wrapper_func(*args, **kwargs):
        print("Wrapper executed this before {}".format(
            original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_func

# Function decorators


@decorator_func  # Equivalent to display = decorator_func(display)
def display():
    print("display function ran")


@decorator_func
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display()
display_info("henry", 3)

# Class Decorator


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method executed this before {}".format(
            self.original_function.__name__))

        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print("display function ran")


@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display()
display_info("henry", 3)


# Decorator applications in Python: Logging

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename="{}".format(
        orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper

# @my_logger
# def display_info(name, age):
# 	print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info('Henry', 4)


import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    # .format(name, age))
    print(f'display_info ran with arguments ({name}, {age})')


print(display_info.__name__)
display_info('James Harden', 13)
