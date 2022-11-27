import re

wiadomosc="To be, or not to be, that is the question "
a=re.findall("[a]",wiadomosc)
e=re.findall("[e]",wiadomosc)
i=re.findall("[i]",wiadomosc)
o=re.findall("[o]",wiadomosc)
u=re.findall("[u]",wiadomosc)
y=re.findall("[y]",wiadomosc)







print(f"samogłosek 'A' w tekscie jest {len(a)}\nsamogłosek 'E' w tekscie jest {len(e)}\nsamogłosek 'i' w tekscie jest {len(i)}\nsamogłosek 'O' w tekscie jest {len(o)}\nsamogłosek 'U' w tekscie jest {len(u)}\nsamogłosek 'y' w tekscie jest {len(y)}")

# A, E, I, O, U, Y