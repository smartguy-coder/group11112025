from typing import Callable


def call_callable(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result

    return inner


@call_callable
def foo() -> int:
    return 10
