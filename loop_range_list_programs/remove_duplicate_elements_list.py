num_list = [12, 13, 15, 18, 20, 12, 15, 18]
unique_list = []
num = num_list[0]

for i in num_list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)


