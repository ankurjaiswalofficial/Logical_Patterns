# Inverted Hollow Full Pyramid

rows = 10

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if ((i + j) >= (rows + 1)):
            if ((i + j) == (rows + 1)) or ((i + j) == (i + rows)) or (i == rows):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print(" ", end="")
    print("")
