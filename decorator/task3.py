
def validate(func):
    def inner(*args):
        for arg in args:
            if arg>256 or arg<0:
                return "Function call is not valid!"
           
        return "Pixel created!"
    return inner


@validate
def set_pixel(a, b, c):
    return a, b, c
    


print(set_pixel(0, 127, 300))
# Function call is not valid!
print(set_pixel(0, 127, 250))
# Pixel created!
