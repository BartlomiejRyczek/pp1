from random import random, randrange, sample, uniform


x=randrange(1,6)
y=randrange(1,6)
z=randrange(1,6)
print(f"Pierwszy rzut kostką: {x}")
print(f"Drugi rzut kostką: {y}")
print(f"Trzeci rzut kostką: {z}")

s=(x+y+z)

print(f"Suma wyrzuconych oczek {s}")
