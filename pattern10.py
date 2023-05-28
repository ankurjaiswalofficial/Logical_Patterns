# Inverted Hollow Left Half Pyramid

rows = 5
for i in range(rows):
    for j in range(rows):
        if (j == i) or (i == 0) or (j == rows - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
