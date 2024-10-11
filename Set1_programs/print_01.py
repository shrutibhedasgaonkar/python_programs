import keyword
import math

# Practice programs
print("Hello")
print("Code Mitra")

print("Hello \n Python")

print("Teacher's Day")

x = 10
y = 'Shruti'
z = 25
print(x, y, z, sep='\n')

name = "Shruti"
age = 37
edu = "B.E(Electronics)"
exp = 11

print("Name = ", name, ", Age = ", age, "years", ", Education = ", edu,
      ", Experience = ", exp, "years")

"""Learning Python is interesting"""

a = 25
b = True
c = "Code Mitra"
d = 5.46
e = 3 + 4j

print(a, b, c, d, e, sep='\n')

q = 12
p = 12
print(id(q), id(p))

print(keyword.kwlist)

# False, None, True keywords are used as data


t = 10
q = str(t)
print(q)
print(type(q))

print(ord('m'))

print(t, hex(t))
print(t, bin(t))
print(t, oct(t))

b = "1100101"
o = int(b, 2)  # convert binary to decimal
print(o)

f = "2F"
h = int(f, 16)  # convert hex to decimal
octal = oct(h)
print(octal)

dec = 125
oct1 = oct(dec)
print(oct1)
"""
name = input("Enter your name = ")
print(name)

num1 = int(input("Enter 1st number = "))
num2 = int(input("Enter 2nd number = "))

Sum = num1 + num2
print("Sum of two numbers is ", Sum)

# Area of Circle
radius = int(input("Enter radius of the circle = "))

Area = math.pi * radius * radius
print("Area of the circle = ", Area)

number = int(input("Enter number = "))
print("Square of the number = ", number * number)

# Area of the triangle
base = int(input("Enter base of the triangle = "))
height = int(input("Enter height of the triangle = "))

Area1 = 0.5 * base * height
print("Area of the triangle = ", Area1)



# Average number
num1 = int(input("Enter 1st number = "))
num2 = int(input("Enter 2nd number = "))
num3 = int(input("Enter 3rd number = "))

average = (num1 + num2 + num3)/2

print("Average of the given numbers = ", average)
"""

# Calculate Simple interest

P = float(input("Enter Principle amount = "))
N = float(input("Enter Period of loan = "))
R = float(input("Enter Rate of Interest = "))

SI = (P * N * R) / 100
print("Simple Interest = ", SI)


