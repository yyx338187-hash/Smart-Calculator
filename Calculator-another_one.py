#Calculator?#
#By MEEEeee#
#Require Python 3.14.7 final#
#Cuz I forgets#
#cd "C:\Users\User\Desktop\Python code\smart-calculator"#
#git status#
#git add .#
#git status#
#git commit -m "Add credits function"#
#git push#
#Yep#

import pyfiglet
import time

figlet = pyfiglet.Figlet(font="standard")
print(figlet.renderText("Smart Calculator"))

def run_tests():
    assert addition(5, 3) == (True, 8), "Addition test 1 failed."
    assert addition(-5, 3) == (True, -2), "Addition test 2 failed."
    assert subtraction(10, 4) == (True, 6), "Subtraction test 1 failed."
    assert subtraction(3, 10) == (True, -7), "Subtraction test 2 failed."
    assert multiplication(6, 7) == (True, 42), "Multiplication test 1 failed."
    assert multiplication(100, 0) == (True, 0), "Multiplication test 2 failed."
    assert division(10, 2) == (True, 5.0), "Division test 1 failed."
    assert division(7, 2) == (True, 3.5), "Division test 2 failed."
    assert division(0, 5) == (True, 0), "Division test 3 failed."
    assert division(10, 0) == (False, "Division by zero is not allowed."), "Division test 4 failed."
    print("All tests passed!")
def end_program():
    while True:
        result = input("\nDo you want to continue? (yes/no) ").lower()
        
        if result not in valids:
            print("\nInvalid input. Please enter 'yes' or 'no'.")
            time.sleep(0.25)
            continue
            
        if result == "no" or result == "end":
            print("\nGood bye!")
            exit()
        elif result == "yes":
            time.sleep(0.25)
            return True
def greet_user(name, greeting="Welcome"):
    print(greeting + ", " + name + "!")
def operation_menu(title="Available operations"):
    symbols = [
        "(+)",
        "(-)",
        "(*)",
        "(/)",
    ]
    available_operations = [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
    ]
    print(f"\n{title}:")
    for number, (symbol, available_operation) in enumerate(zip(symbols, available_operations), start=1):
        print(f"{number}. {available_operation}{symbol}")
def addition(num1, num2):
    return True, num1 + num2
def subtraction(num1, num2):
    return True, num1 - num2
def multiplication(num1, num2):
    return True, num1 * num2
def division(num1, num2):
    if num2 == 0:
        return False, "Division by zero is not allowed."
    return True, num1 / num2
operation_functions = {
    "+": addition,
    "addition": addition,
    "1": addition,

    "-": subtraction,
    "subtraction": subtraction,
    "2": subtraction,

    "*": multiplication,
    "multiplication": multiplication,
    "3": multiplication,

    "/": division,
    "division": division,
    "4": division,
}
valids = {
    "yes",
    "no",
    "end",
    }

time.sleep(1.25)
name = input("\nWelcome to Smart Calculator!\n\nWhat is your name? ")
greet_user(name)

while True:
    try:
        number1 = input("\nEnter your first number: ").lower()
        if number1 == "end":
            exit()
        number1 = float(number1)
        
        operation_menu()
        operation = input("\nChoose calculation: ").lower()
        if operation == "end":
            exit()
        if operation not in operation_functions:
            print("\nInvalid operation.")
            continue
            
        number2 = input("\nEnter your second number: ").lower()
        if number2 == "end":
            exit()
        number2 = float(number2)
        
        selected_function = operation_functions[operation]
        a, b = selected_function(number1, number2)
        
        if a:
            print("\nThe result is: " + str(b))
        else:
            print("\nError: " + str(b))
            
        time.sleep(0.75)
        
        end_program()
        
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")
        continue