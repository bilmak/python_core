from datetime import datetime
from time import sleep


def log(func):
    def inner(*args, **kwargs):
        time_start = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        diff = round((end_time - time_start).total_seconds(), 5)
        with open("task2.txt", "w")as f:
            f.write(
                f"{func.__name__}; args:{args}; kwargs: {kwargs}; execution time: {diff} sec. Result = {result}")
        return result

    return inner


@log
def foo(a, b, c):
    sleep(1)
    return a+b+c


foo(1, 2, c=3)
