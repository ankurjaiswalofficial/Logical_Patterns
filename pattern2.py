# Hollow Rectangle


rows = 5
columns = 8

for i in range(rows):
    for j in range(columns):
        if (j == 0) or (j == columns - 1) or (i == 0) or (i == rows - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
