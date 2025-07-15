def divide(text: str):
    try:
        i, y = text.split()
        result = int(i)/int(y)
        return result
    except Exception as e:
        return f"Error code: {e}"
        

print(divide("4     2"))
# 2.0

print(divide("4 0"))
# "Error code: division by zero"

print(divide("* 1"))
# "Error code: invalid literal for int() with base 10: '*'"
