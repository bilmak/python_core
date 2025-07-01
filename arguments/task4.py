def combine_dicts(*args: dict) -> dict:
    result: dict = {}
    for dicts in args:
        for k, v in dicts.items():
            if k not in result:
                result[k] = 0
            result[k] += v
    print(result)


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
# {'a': 300, 'b': 200, 'c': 300}

print(combine_dicts(dict_1, dict_2, dict_3))
# {'a': 600, 'b': 200, 'c': 300, 'd': 100}
