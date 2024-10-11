x = float(input(" Enter X Co-ordinate = "))
y = float(input(" Enter Y Co-ordinate = "))

if x > 0 and y > 0:
    print("Co-ordinates X =", x, "and Y =", y, "lies in First Quadrant")

elif x < 0 < y:
    print("Co-ordinates X =", x, "and Y =", y, "lies in Second Quadrant")

elif x < 0 and y < 0:
    print("Co-ordinates X =", x, "and Y =", y, "lies in Third Quadrant")

else:
    print("Co-ordinates X =", x, "and Y =", y, "lies in Fourth Quadrant")

