from random import randrange


y=randrange(1,6)
print("Komputer rzuca kostką...")
x=input("Odgadnij wyrzuconą ilość oczek: ")
zgadnij_numer=float(x)

print(zgadnij_numer==y)
