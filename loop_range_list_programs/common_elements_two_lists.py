list1 = [23, 54, 67, 12, 100, 50, 80]
list2 = [100, 23, 50, 16, 80, 75, 15]
common_list = []

for i in list1:
    if i in list2:
        common_list.append(i)

print("List of common elements from two lists = ", common_list)

