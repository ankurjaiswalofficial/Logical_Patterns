# Hollow Left Half Pyramid

rows = 5

for i in range(rows - 1, -1, -1):
    for j in range(rows):
        if (j == i) or (j == rows - 1) or (i == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()