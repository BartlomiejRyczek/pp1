x=str(input("Podaj nazwę pliku: "))
wiersze=0
f = open(x)
for line in f:
     wiersze+=1
print(wiersze)
f.close()
