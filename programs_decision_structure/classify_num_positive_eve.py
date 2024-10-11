num = float(input(" Enter any number = "))

if num > 0 and num % 2 == 0:
    print(num, " is a positive Even Number")

elif num > 0 and num % 2 != 0:
    print(num, " is a positive Odd Number")

elif num < 0 and num % 2 == 0:
    print(num, " is a negative Even Number")

else:
    print(num, " is a negative Odd Number")
