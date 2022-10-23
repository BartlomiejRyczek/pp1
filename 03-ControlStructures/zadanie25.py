for i in range(4):
    for j in range(16):
        if (j==0 or j==15) or (i==0 or i==3) and (j>0 and j<15):
            print("*", end="")
        else:
            print(end=" ")
    print()