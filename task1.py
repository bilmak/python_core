def get_fractions(a_b:str, c_d:str)-> str:
    x, y = a_b.split("/")
    i, j = c_d.split("/")
    x = int(x)
    y = int(y)
    i = int(i)
    j = int(j)
    if y != j:
        return "Denominators are not the same"
    result = x + i
    return f"{result}/{j}"    
    
    
a_b = '1/3'
c_b = '5/3'
print(get_fractions(a_b, c_b))
    