from time import sleep
from datetime import timedelta, datetime

execution_time: dict = {}


def time_decorator(func):
    def wrapped(*args):
        time_start = datetime.now()
        func(*args)
        time_end = datetime.now()
        diff = time_end-time_start
        execution_time[func.__name__] = str(diff)
    return wrapped


@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b


func_add(10, 20)

print(execution_time)
# 0.212341254
