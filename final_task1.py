
def unique_values_dict(main: list[dict]) -> set:
    result_list: list = []
    for items in main:
        for _, v in items.items():
            if v in result_list:
                continue

            result_list.append(v)

    print(set(result_list))
    return set(result_list)


unique_values_dict([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
                   "VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}])


# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
