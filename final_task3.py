def split(data: str, sep=None, maxsplit=-1) -> list:
    result: list = []
    subresult = ""
    count: int = 0
    if sep is None:
        sep = " "
    for i, letter in enumerate(data):
        if letter == sep:
            if subresult:
                result.append(subresult)
                count += 1
                if count == maxsplit:
                    result.append(data[i:])
                    return result
                subresult = ""
            continue
        subresult += letter
    if subresult:
        result.append(subresult)
        count += 1

    return result


print(split('    Hi    Python    world! exit', maxsplit=2))
# ['Hi', 'Python', 'world!']
