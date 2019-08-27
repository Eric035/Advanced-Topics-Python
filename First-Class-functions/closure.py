# Closure: sample code
import logging

def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

tony_func = outer_func('Tony')
eric_func = outer_func('Eric')

tony_func()
eric_func()

