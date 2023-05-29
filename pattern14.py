# Inverted Hollow Full Pyramid

rows = 5


for i in range(0, rows):
    for j in range(0, rows):
        if (i > j):
            print(" ", end="")
        else:
            if j == i or i == 0 or j == rows - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()