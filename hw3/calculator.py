def addition(value1, value2):
    return value1+value2

def subtraction(value1, value2):
    return value1-value2

def multiplication(value1, value2):
    return value1*value2

def division(value1, value2):
    if value2==0:
        return 0
    if value1%value2==0:
        return value1/value2
    else:
        return str(value1//value2)+','+str(value1%value2)

print(addition(2, 3))
print(subtraction(9, 3))
print(multiplication(3, 3))
print(division(10, 8))