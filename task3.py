from functools import wraps

def mock(return_value="Ну нет"):
    def deb(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return return_value
        return wrapper
    return deb

@mock()
def f(x):
    return x

if __name__ == "__main__":
    print(f(1))