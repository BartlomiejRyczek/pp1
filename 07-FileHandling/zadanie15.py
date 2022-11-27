enter=input("Kliknij enter by wyswietlic kolejne 5 wersów: ")

file = open('filename.txt','r', encoding="UTF-8")

liczba=0

for line in file:
    print(line)
    liczba+=1
    if liczba%5==0:
        try:
            input("Nacisnij enter by pokazac kolejne 5 linijek kodu")
        except:
            break