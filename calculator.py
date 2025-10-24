

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0 or num1 == 0:
        return float('inf')
    return num1 / num2
def add(num1, num2):
        return num1 + num2

if __name__== "__main__":
    print("Welcome to the calculator. I would rather be anywhere else.\nenter ur numbers or something")
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    user_input = input("ok whadda ya want to do\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n").lower()

    if user_input in ('1', 'add', 'plus', '+'):
        print(add(number1, number2))
    elif user_input in ('2', 'subtract', 'minus', '-'):
        print(subtract(number1, number2))
    elif user_input in ('3', 'multiply', 'times', '*'):
        print(multiply(number1, number2))
    elif user_input in ('4', 'divide', '/'):
        if number2 != 0:
            print(divide(number1, number2))
        else:
            print("yeah cant do that lmao.")
    print("done i guess")