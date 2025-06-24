
def get_longest_word(s:str):
    longestWord:str = ""
    words = s.split()
    for word in words:
        if len(word)>len(longestWord):
            longestWord = word
        
    print(longestWord)
    

get_longest_word('Python is simple and effective!')