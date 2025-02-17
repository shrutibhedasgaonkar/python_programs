
user_input = int(input("Enter the number = "))
factor = 1
i = 1

for i in range(1, user_input + 1):
    factor = factor * i
    print(i, end=" ")

print(end="\n")
print("The factorial = ", factor)

