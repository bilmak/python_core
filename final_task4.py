def split_by_index(data: str, args: list[int]) -> list[str]:
    result: list = []
    word: str = ""
    for k, v in enumerate(data, start=1):
        word += v
        if k in args:
            result.append(word)
            word = ""
    if word:
        result.append(word)
        word = ""
    return result


# print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
# ["python", "is", "cool", ",", "isn't", "it?"]
print(split_by_index("no luck", [42]))
# ["no luck"]
