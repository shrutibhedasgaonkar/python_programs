age = int(input("Enter your current age = "))

if age >= 18:
    weight = float(input("Enter your weight (in Kg) = "))
    height = float(input("Enter you height (in meters) = "))

    BMI = weight / (height * height)  # Calculates BMI

    if BMI < 18.5:
        print("Your BMI is ", f"{BMI: .2f}", "\nYou are Under weight")

    elif 18.5 <= BMI < 24.9:
        print("Your BMI is ", f"{BMI: .2f}", "\nYou have Normal weight")

    elif 25 <= BMI < 29.9:
        print("Your BMI is ", f"{BMI: .2f}", "\nYou are Over weight")

    else:
        print("Your BMI is ", f"{BMI: .2f}", "\nYou are Obese")
else:
    print("BMI categories do not apply to minors, you should be at-least 18 years old ")
