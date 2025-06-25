def foo(nums: list) -> list:

    result: list = []
    for i in nums:
        product: int = 1
        for j in nums:
            if i != j:
                product *= j
        result.append(product)

    print(result)
    return result


def foo2(nums: list) -> list:
    product: int = 1
    result: list = []
    for i in nums:
        product *= i
    for i in nums:
        num = product/i
        result.append(int(num))
    print(result)


foo2([1, 2, 3, 4, 5])
