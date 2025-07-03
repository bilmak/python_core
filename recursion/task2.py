def linear_seq(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple, set)):
            result.extend(linear_seq(item))
        else:
            result.append(item)
    return result


sequence = [1, 2, 3, [4, 5, (6, 7)]]

print(linear_seq(sequence))
# [1, 2,3,4,5,6,7]
