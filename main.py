def addition(num1, num2):
    return f'Result: {num1 + num2}'

def subtraction(num1, num2):
    return f'Result {num1 - num2}'

def multiplication(num1, num2):
    return f'Result {num1 * num2}'

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Numbers cannot be divided by zero.")

while True:
    symbol = input("Math symbol: ")
    if symbol in ("+","-","*","/"):
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Enter second number: "))
        except ValueError: 
            print("Invalid numbers, try again")
            continue
    
        match symbol:
            case "+":
                print(addition(num1,num2))
            case "-":
                print(subtraction(num1, num2))
            case "*":
                print(multiplication(num1, num2))
            case "/":
                print(division(num1,num2))
        next_calculation = input("Do you want to continoues: [y,n]: ")
        if next_calculation == "n":
            break
    else:
        print("Invalid input")