def matrix(row_start: int, row_end: int, column_start: int, column_end: int) -> list[list]:
    result = []

    for i in range(row_start, row_end+1):
        sub_result = []
        for j in range(column_start, column_end+1):
            product = i*j
            sub_result.append(product)
        result.append(sub_result)
    print(result)


matrix(row_start=2, row_end=4, column_start=3, column_end=7)
