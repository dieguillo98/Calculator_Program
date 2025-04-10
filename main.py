def addition(x,y):
    return f'Result: {x + y}'

def subtraction(x,y):
    return f'Result: {x - y}'

def multiplication(x,y):
    return f'Result: {x * y}'

def division(x,y):
    try:
        return f'Result {x / y}'
    except ZeroDivisionError:
        return f'Numbers cannot be divided by zero'

while True:
    symbol = input('Math symbol: ')
    if symbol in ('+','-','*','/'):
        try:
            num1 = float(input('First number: '))
            num2 = float(input('Second number: '))
        except ValueError:
            print('Invalid numbers, try again')
            continue

        match symbol:
            case  '+':
                print(addition(num1, num2))
            
            case '-':
                print(subtraction(num1, num2))

            case '*':
                print(multiplication(num1, num2))
            
            case '/':
                print(division(num1, num2))

        
        next_operation = input("Do you want to continue? [y,n]: ")
        if next_operation == 'y':
            continue
        else:
            print("Bye, Bye!")
            break
    print("Invalid input")
