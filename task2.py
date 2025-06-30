def query(data, *args):
    for k in args:
        rows = k(data)
        print(k(data))

    data = select('name', 'gender', 'sport')(friends)

    data = field_filter('sport', *('Basketball', 'Volleyball'))(data)
    data = field_filter('gender', *('male',))(data)


def select(*args):
    def inner(data: list[dict]) -> list[dict]:
        result: list[dict] = []
        for row in data:
            data_dict: dict = {}
            for k, v in row.items():
                if k in args:
                    data_dict[k] = v
            result.append(data_dict)
        return result
    return inner


def field_filter(key, *args):
    def inner(data: list[dict]) -> list[dict]:
        result: list[dict] = []
        for row in data:
            if row[key] in args:
                result.append(row)
        return result
    return inner


friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'},
]
query(friends, select('name', 'gender', 'sport'),
      field_filter('sport', *('Basketball', 'Volleyball')),
      field_filter('gender', *('male',)))
