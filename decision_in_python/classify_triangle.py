side1 = float(input(" Enter length of side 1 = "))
side2 = float(input(" Enter length of side 2 = "))
side3 = float(input(" Enter length of side 3 = "))

if side1 == side2 == side3:
    print("As the length of 3 sides are equal, triangle is Equilateral triangle")

elif (side1 != side2) and (side2 != side3) and (side1 != side3):
    print("As the length of 3 sides are not equal, triangle is Scalene triangle")

elif (side1 == side2) or (side2 == side3) or (side1 == side3):
    print("As the length of 2 sides are equal, triangle is Isosceles triangle")
