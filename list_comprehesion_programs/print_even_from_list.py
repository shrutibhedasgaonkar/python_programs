numbers = [2, 3, 4, 6, 8, 22, 5, 11, 41, 88, 7, 34, 50]
'''
for even in numbers:
    if even % 2 == 0:
        print(f'{even} is even number')'''

even_num = [i for i in numbers if i % 2 == 0]
print(even_num)
