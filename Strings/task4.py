import re


def palidrome(word:str)->bool:
    to_lower = str.lower(word)
    formated_spaces = to_lower.replace(" ","")
    regexp = re.sub(r'[^a-zA-Zа-яА-Я\s]', '', formated_spaces)
    
    length= len(regexp)
    for i in range(0, length//2):
        if regexp[i]!=regexp[length-i-1]:
            return False
    
    return True
    
    
    
    
result = palidrome("A dog! A panic in a pagoda!")
print(result)