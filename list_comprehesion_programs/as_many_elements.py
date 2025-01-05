''' Using for loop '''
num_list = []
count = int(input(" Enter how many number do you want to enter = "))

for _ in range(count):
    user_input = int(input("Enter Number: "))
    num_list.append(user_input)

print(num_list)


''' Using while loop '''
num_list1 = []
count1 = int(input(" Enter how many number do you want to enter = "))
i = 0
while i < count1:
    user_input1 = int(input("Enter Number: "))
    num_list1.append(user_input1)
    i += 1

print(num_list1)
