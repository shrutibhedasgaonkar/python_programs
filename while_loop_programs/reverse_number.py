x = int(input("Enter any number = "))
reverse_num = 0

while x > 0:
    last_digit = x % 10
    reverse_num = reverse_num * 10 + last_digit
    x //= 10
print("Reversed number is", reverse_num)

