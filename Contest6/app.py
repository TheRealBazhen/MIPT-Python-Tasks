import functools


class VeryImportantClass:
    def __init__(self):
        self.a = 1
        self.s = "fidflk"
        self.c = [0, 1, 1]
        self._ooo = [4]

    def method(self):
        print("Method called")
        print(self.a)


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator")
        return func(*args, **kwargs)
    return wrapper
