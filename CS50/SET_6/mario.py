size = int(input("Height: "))

row = 1
for i in range(size):
    for j in range(size - row):
        print(" ", end="")
    
    for k in range(row * 2):
        print("#", end="")
        if k == (row - 1):
            print("  ", end="")

    print()
    row += 1
