year = int(input("Enter your choice of year = "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Entered Year is a leap year")

else:
    print("Entered Year is not a leap year.")
