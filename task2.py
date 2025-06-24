def fizz_buzz(lst: list[int]) -> list:
    result: list = []

    for n in lst:

        if n % 3 == 0 and n % 5 == 0:
            result.append("FizzBuzz")
        elif n % 5 == 0:
            result.append("Buzz")
        elif n % 3 == 0:
            result.append("Fizz")
        else:
            continue

    print(result)
    return result


fizz_buzz([4, 6, 2, 8, 24, 657, 23, 65, 5, 45, 5, 15])
