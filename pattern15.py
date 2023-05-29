# Number Pyramid Palindromic Style

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(j + 1, end=" ")
    for k in range(i, 1, -1):
        print(k - 1, end=" ")
    print()