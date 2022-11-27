f=open("shoppinglist.txt")


with open("grainsandbread.txt", "a") as f:
    for line in f:
        f.write("shoppinglist.txt ")
    with open("meatandfish.txt", "a") as f1:
        for line in f:
            f.write("shoppinglist.txt")