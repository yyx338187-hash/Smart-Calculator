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

def title_text():
    print(figlet.renderText("Smart Calculator"))
def credits():
    print("\nThis calculator was created by MEEEeee.")
    time.sleep(0.5)
    print("Version: 1.0.0")
    time.sleep(0.5)
    print("Release Date: 2024-06-01")
def greet_user(name):
    print("Hello, " + name + "!")
def operation_menu():
    print("\nAvailable operations:")
    print("+ addition")
    print("- subtraction")
    print("* multiplication")
    print("/ division")
def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
def main():
    while True:

        try:
            number1 = input("\nEnter your first number:  ").lower()
            if number1 == "end":break
            number1 = float(number1)

            operation_menu()

            operation = input("\nChoose calculation:  ").lower()

            if operation not in ["+", "addition", "-", "subtraction", "*", "multiplication", "/", "division"]:
                print("\nInvalid operation.")
                continue
            number2 = input("\nEnter your second number:  ").lower()
            if number2 == "end":
                break
            number2 = float(number2)

            if operation in ["+", "addition"]:
                result = addition(number1, number2)
                print("\nThe result is:\n" + str(result))
            elif operation in ["-", "subtraction"]:
                result = subtraction(number1, number2)
                print("\nThe result is:\n" + str(result))
            elif operation in ["*", "multiplication"]:
                result = multiplication(number1, number2)
                print("\nThe result is:\n" + str(result))
            elif operation in ["/", "division"]:
                result = division(number1, number2)
                print("\nThe result is:\n" + str(result))
            continue_calculation = input("\nWould you like another calculation?\nEnter 'yes' or 'no':  ").lower()
            if continue_calculation == "yes":
                continue
            elif continue_calculation == "no":
                print("\nGood bye, " + name + "!")
                break
            else:
                print("\nInvalid input. Exiting the calculator.")
                break
                
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            break

time.sleep(1.25)

Haha = input("R u from TISKL?\n\nEnter 'yes' or 'no':  ").lower()

if Haha == "yes":
    print("\n*Evil laugh*")
    time.sleep(1.25)
    print("\nWELCOME...")
    main()
else:
    print("Welcome to the Smart Calculator!")

name = input("\nWelcome to Smart Calculator!\n\nWhat is your name?  ")
if name.lower() == "end":
    print("\nGood bye!")
    exit()

greet_user(name)

credits()

main()