# Left Half Pyramid

rows = 5

for i in range(rows - 1, -1, -1):
    for j in range(rows):
        if (j == i) or (j > i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
