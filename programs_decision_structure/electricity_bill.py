unit = float(input("Enter units consumed = "))

if unit >= 0:
    if unit <= 100:
        bill = 5 * unit
        print("As you have consumed ", unit, "units, your electricity bill is Rs.", bill)

    elif 101 < unit <= 200:
        bill = 7 * unit
        print("As you have consumed ", unit, "units, your electricity bill is Rs.", bill)

    else:
        bill = 10 * unit
        print("As you have consumed ", unit, "units, your electricity bill is Rs.", bill)

else:
    print("You have entered invalid input")
