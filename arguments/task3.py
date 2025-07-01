def union(*args) -> set:
    result = set()
    for row in args:
        for item in row:
            result.add(item)
    return result


def intersect(*args) -> set:
    result = set(args[0])
    for row in args[1:]:
        result = result.intersection(row)

    return result


union(('S', 'A', 'M'), ['S', 'P', 'A', 'C'])
# {'S', 'P', 'A', 'M', 'C'}
intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C'))
# {'S', 'C'}
