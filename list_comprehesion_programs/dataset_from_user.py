count = int(input("how many numbers do you want to store = "))

"""
new = []
for i in range(count):
    num = input("Enter number = ")
    new.append(num)

print(new)

"""

new = [int(input("Enter number = ")) for i in range(count)]
print(new)
