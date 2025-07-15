class Counter():
    def __init__(self, data):
        self.data = data

    def __add__(self, text):
        result = []
        for i in self.data:
            result.append(str(i) + text)

        return result


c = Counter([1, 2, 3])
print(c+" Misisispi")
