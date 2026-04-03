from warnings import warn
from functools import wraps

def deprecated(s):
    def deb(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            warn(s)
            return f(*args, **kwargs)
        return wrapper
    return deb

@deprecated("ляляля")
def f(x):
    return x
if __name__ == "__main__":
    print(f(1))