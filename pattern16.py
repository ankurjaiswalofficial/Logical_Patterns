# Number Pyramid Palindromic Style

rows = 5

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if ((i + j) >= (rows + 1)):
            print(rows + 1 - j, end=" ")
        else:
            print(" ", end="")
    for j in range(rows + 1, 1, -1):
        if ((i + j) >= (rows + 1)):
            print(rows - j, end=" ")
        else:
            print(" ", end="")
    print()
