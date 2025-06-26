def vowel_frequency(s: str) -> dict:
    main: dict = {}
    lower = s.lower()
    vowel_letters = ['e', 'o', 'i', 'u', "a"]
    for v in lower:
        if v not in main and v in vowel_letters:
            main[v] = 0
        if v in vowel_letters:
            main[v] += 1

    print(main)
    return main


vowel_frequency("Education is important")
