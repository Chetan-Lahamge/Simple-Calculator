from termcolor import colored

text = "Welcome to the Simple Calculator!\n"
colored_text = colored(text, color='white', attrs=['bold', 'underline'])
print(colored_text)

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
operation = int(input("Please select the operation:\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Exit "))

def calculator(num1, num2, operation):
    if operation == 1:
        result = num1 + num2
        operator = "Addition"
    elif operation == 2:
        result = num1 - num2
        operator = "Substraction"
    elif operation == 3:
        result = num1 * num2
        operator = "Multiplication"
    elif operation == 4:
        if num2 != 0:
            result = num1 / num2
            operator = "Division"
        else:
            print("Error: Cannot divide by zero")
            exit(0)
    else:
        print("Exited From Calculator")
        exit(0)

    print(f"{operator} of Numbers = {result}")

calculator(num1, num2, operation)