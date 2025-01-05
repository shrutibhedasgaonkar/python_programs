def left_triangle_pattern(x, ch):
    for i in range(0, x + 1):
        for j in range(i):
            print(ch, end=' ')

        print()


row_num = int(input("Enter number of rows = "))
character = input("Enter character to print = ")

left_triangle_pattern(row_num, character)
