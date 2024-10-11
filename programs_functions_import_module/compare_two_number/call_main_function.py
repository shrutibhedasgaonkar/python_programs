from compare_small_greater import *


# Prompt the user to input the first number and second number and convert it to float
num1 = float(input("Enter 1st number to compare = "))
num2 = float(input("Enter 2nd number to compare = "))

# Call the function compare_s_to_g to find the greater number between num1 and num2
result = compare_s_to_g(num1, num2)

# Print the result, indicating which number is greater
print("from", num1, "and ", num2, ",", result, "is greater")
