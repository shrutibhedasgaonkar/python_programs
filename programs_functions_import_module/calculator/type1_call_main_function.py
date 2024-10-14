from type1_calc import *

num1 = float(input(" Enter first number = "))
num2 = float(input(" Enter second number = "))

addition = add(num1, num2)
print("Addition of ", num1, "and ", num2, "is ", addition)

subtraction = sub(num1, num2)
print("Subtraction of ", num1, "and ", num2, "is ", subtraction)

multiplication = multi(num1, num2)
print("Multiplication of ", num1, "and ", num2, "is ", multiplication)

division = divi(num1, num2)
print("Division of ", num1, "and ", num2, "is ", division)

modulus = mod1(num1, num2)
print("MOD of ", num1, "and ", num2, "is ", modulus)

