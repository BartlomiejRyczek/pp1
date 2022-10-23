x=int(input("Podaj kwotę: "))


calosci=x//5
reszta=x%5

calosci1=reszta//2
reszta1=reszta%2

print(f"Kwota {x} w monetach 5zł - {calosci}, 2zł - {calosci1} i 1zł - {reszta1}")
