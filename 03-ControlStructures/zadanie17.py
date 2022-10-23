x=int(input("Podaj liczbę: "))
y=int(input("Podaj liczbę: "))

if (x==0 and y==0):
    print(f"Punkt P({x}, {y}) znajduję się w punkcie układu współrzędnych")

if (x>0 and y>0):
    print(f"Punkt P({x}, {y}) znajduje się w I ćwiartce")

if (x<0 and y<0):
    print(f"Punkt P({x}, {y}) znajduje się w II ćwiartce")

if (x<0 and y<0):
    print(f"Punkt P({x}, {y}) znajduje się w III ćwiartce")

if (x>0 and y<0):
    print(f"Punkt P({x}, {y}) znajduje się w IV ćwiartce")
