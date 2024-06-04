""" BMI Calculator
A program that calculates the Body Mass Index (BMI) from a user's weight and height

Divides weight (in kg) by the square of their height(in m)

BMI = weight(kg)/(height*height)
"""

height = float(input("What is your height in meters? "))  # Get user's height
weight = float(input("What is your weight in kg? "))   # Get user's weight

BMI = int(weight / (height * height))

print("Your BMI is: ", BMI)
