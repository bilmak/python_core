def generate_squares(n: int) -> dict:
    result: dict = {}
    for i in range(1, n+1):
        if i not in result:
            result[i] = 1
        result[i] = i*i

    print(result)


generate_squares(5)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
