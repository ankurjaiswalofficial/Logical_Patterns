# Inverted Hollow Right Half Pyramid

rows = 5

for i in range(rows - 1, -1, -1):
    for j in range(i + 1):
        if (j == 0) or (j == i) or (i == rows - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()