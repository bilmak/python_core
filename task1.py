def seq_sum(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple, set)):
            result += seq_sum(item)
        else:
            result += item
    return result


sequence = [1, 2, 3, [4, 5, (6, 7)]]
print(seq_sum(sequence))
# 28
