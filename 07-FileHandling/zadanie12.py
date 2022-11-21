file=open("shopping.txt")

for i in range(5):
    groseries=input(":")
    file.write(f"{groseries}\n")
file.close()