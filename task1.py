def frequency_letter(s: str) -> dict:
    result: dict = {}

    new_string = s.lower()
    for v in new_string:
        if v not in result:
            result[v] = 0
        result[v] += 1

    if not result:
        print("Dict is empty")

    print(result)


frequency_letter('Oh, it is python')
