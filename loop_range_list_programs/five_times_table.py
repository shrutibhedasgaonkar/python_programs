""" Using list
list_one = []
i = 0
for i in range(5, 55, 5):
    list_one.append(i)
    i += 1

print(list_one)
"""

"""Using list comprehension
list_num = []
i = 0
times_table = [i for i in range(5, 55, 5)]
print(times_table)
"""

""" Using simple while 
i = 1
while i < 11:
    print(i * 5)
    i += 1
"""

"""Using user input 
user_input = int(input("Which times table do you want? ="))
i = 1
while i < 11:
    print(i * user_input)
    i += 1
"""

""" Using user input and list comprehesion """
user_input = input("Which times table do you want? =")
i = 1
times_table1 = [i for i in range(int(user_input), (int(user_input) * 11), int(user_input))]
print(times_table1)

