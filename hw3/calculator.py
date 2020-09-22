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



while True:
    x = input('What would you like to do? ')
    
    if x == 'done':
        print('Thanks for using my calculator')
        break

    y = int(input('Enter value1 '))
    z = int(input('Enter value2 '))

    if x == 'add':
        print(addition(y,z))

    if x == 'subtract':
        print(subtraction(y, z))

    if x == 'multiply':
        print(multiplication(y, z))

    if x == 'divide':
        print(division(y, z))