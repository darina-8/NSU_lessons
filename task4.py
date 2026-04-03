def wraps(f):
    def decor(wrapper):
        wrapper.__name__ = f.__name__
        wrapper.__doc__ = f.__doc__
        wrapper.__module__ = f.__module__
        return wrapper
    return decor


def trace(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        print(f'{f.__name__}, arguments: {args}, kwargs: {kwargs}, res: {res}')
        return res
    return wrapper


@trace
def say_hi():
    '''I'm stupid func'''
    print('hi')

if __name__ == "__main__":
    say_hi()