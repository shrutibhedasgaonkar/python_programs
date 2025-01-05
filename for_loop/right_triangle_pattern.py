def left_triangle(x, ch):
    for i in range(1, x + 1):
        for j in range(x - i):
            print(" ", end=' ')

        for j in range(i):
            print(ch, end=' ')

        print()


row_num = int(input("Enter number of rows = "))
character = input("Enter character to be printed = ")

left_triangle(row_num, character)
