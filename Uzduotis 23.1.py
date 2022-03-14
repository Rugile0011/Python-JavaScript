from functools import wraps

def argument_limiter(func):
    def wrapper(*args, **kwargs):
        if len(args) <= 2:
            return True
        else:
            return False
    return wrapper

from time import sleep

def delay(time):
    def delay_again(fn):
        def wrapper(*args, **kwargs):
            sleep(time)
            print(f"Funkcija atideta {time} sek")
            return fn(*args, **kwargs)
        return wrapper
    return delay_again

def strings_only(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) != str:
                raise TypeError("Text is not string!")
            return func(*args)
        return wrapper


@delay(3)
def late(text):
    return text

print(late(3))

