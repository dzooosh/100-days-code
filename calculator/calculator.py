#!/usr/bin/python3

""" CALCULATOR APP
    This is a simple calculator app

Create add, subtract, multiply, divide function on another file and import
 assign each operator to a keyboard key using dictionary e.g div : '/', multiple: '*'...
 Get user input with num1, num2 and operator
 use the operator to perform the operation on the input values
 display the result
 ask to continue or not
"""
from calculatorart import logo
from ops import add, subtract, multiply, divide


print(logo)

# Operator dictionary
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Get user input
opt = input("Enter the operators '+', '-', '*', '/': ")
n1 = int(input("Enter the first num: "))
n2 = int(input("Enter the second num: "))

# use while loop to continue
continue_with_total = True

while continue_with_total == True:
    # Perform the operation
    result = operators[opt](n1, n2)
    print(f"{n1} {opt} {n2} = {result}")
    # Ask to continue or not
    check = input("Do you want to continue? Type 'y' or 'n'? ")
    
    if check == "y":
        opt = input("Enter the operators '+', '-', '*', '/': ")
        n1 = result
        n2 = int(input("Enter number: "))
    elif check == "n":
        continue_with_total = False
        print(f"The total is {result}")
        print("Thank you for using the calculator")
    else: # if user inputs anything else except 'y' and 'n'
        print("Invalid input")
