def anagram(word1: str, word2: str) -> bool:
    dict_word1: dict = {}
    dict_word2: dict = {}

    for v in word1:
        if v not in dict_word1:
            dict_word1[v] = 0
        dict_word1[v] += 1

    for v in word2:
        if v not in dict_word2:
            dict_word2[v] = 0
        dict_word2[v] += 1

    if dict_word1 == dict_word2:
        return True

    return False


a = anagram('lsten', 'silent')
print(a)
