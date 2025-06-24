def sorted_list(words: list)->list:
    unique_list:list = []
    for word in words:
        if word in unique_list:
            continue
        else:
            unique_list.append(word)
         
    sorted_list:list = sorted(unique_list, key=len ,reverse=True)
    print(sorted_list)
    return sorted_list
    
    
sorted_list(['red', 'white', 'black', 'red', 'green', 'black'])
