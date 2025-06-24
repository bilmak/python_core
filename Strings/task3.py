def replacer(word:str):
    result = ""
    for s in word:
        if s == '"':
            result += "'"
        elif s == "'":
            result +='"'
        else:
            result+=s
            
    print(result)
            
replacer("hel't'")
