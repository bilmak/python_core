def most_frequent_letter(s: str) -> str:
    main: dict = {}

    for v in s:
        if v not in main:
            main[v] = 0
        main[v] += 1

    count: int = 0
    letter_key: str = ""
    for k, v in main.items():
        if v > count:
            count = v
            letter_key = k
    return letter_key


most_frequent_letter('successes')
