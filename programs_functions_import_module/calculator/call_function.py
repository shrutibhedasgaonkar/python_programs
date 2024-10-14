from auto_calc import *


num1 = float(input(" Enter first number = "))
num2 = float(input(" Enter second number = "))
operator = input("Enter the operator from "
                 "+ or "
                 "- or "
                 "* or "
                 "/ or "
                 "% :- ")

result = calc(num1, num2, operator)

print(num1, operator, num2, "=", result)


