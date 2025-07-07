def split(data: str, sep=None, maxsplit=-1) -> list:
    result: list = []
    subresult = ""
    for letter in data:
        if letter == " ":
            if subresult:
                result.append(subresult)
                subresult = ""
            continue
        subresult += letter
    if subresult:
        result.append(subresult)
    print(result)
    return result


split('    Hi    Python    world!', " ", -1)
# ['Hi', 'Python', 'world!']
