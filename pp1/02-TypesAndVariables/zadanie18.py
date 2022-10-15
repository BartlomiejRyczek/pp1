a=input("Podaj wymiary boku a: ")
bok_a=float(a)

b=input("Podaj wymiary boku b: ")
bok_b=float(b)

c=input("Podaj wymiary boku c: ")
bok_c=float(c)

p=(bok_a+bok_b+bok_c)/2

import math

S=(p*(p-bok_a)*(p-bok_b)*(p-bok_c))

print(f"Pole trójkąta wynosi {math.sqrt(S)}")
