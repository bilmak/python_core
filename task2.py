def frequency_word(s: str) -> dict:
    new_string = s.lower()
    string_for_dict = new_string.split(" ")
    result: dict = {}
    for v in string_for_dict:
        if v not in result:
            result[v] = 0
        result[v] += 1

    return result


frequency_word('Python is fun and Python is powerful')
