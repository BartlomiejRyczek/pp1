suma=0
x=-1
while True:
    line = int(input('Podaj liczbę: '))
    x=x+1
    suma=suma+line

    if line == 0:
        sred=suma/x
        print(f"Ilość wpisanych liczb {x}, suma podanych liczb {suma}, srednia podanych liczb {sred}")
        break