from warnings import warn
from functools import wraps


def deprecated(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        warn("Dont ise me i am outdated!!!")
        return f(*args, **kwargs)
    return wrapper

@deprecated
def f(x):
    return x
if __name__ == "__main__":
    print(f(1))