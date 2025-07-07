def decorator_apply(function):  # lambda user_id: user_id + 1
    def real_decorator(func):  # return_user_id
        def inner(num: int):
            result = function(num)
            user = func(result)
            return user
        return inner
    return real_decorator


decorator = decorator_apply(lambda user_id: user_id + 1)


@decorator
def return_user_id(num: int):
    return num


print(return_user_id(42))
# 43
