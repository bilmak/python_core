def get_tuple(num: int) -> tuple[int]:
    result = []
    for i in str(num):
        result.append(i)

    answer = tuple(result)
    print(answer)
    return answer


get_tuple(456)
